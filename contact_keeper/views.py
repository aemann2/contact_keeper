from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.db.models import Q
from .models import Contact, User
from .forms import ContactForm


@login_required
def home(request):
    if request.POST:
        # create form instance w/ POST data, validate, attach user, and save
        form = ContactForm(request.POST)
        form.owner = request.user
        if form.is_valid():
            form.save()
            # reset form
            form = ContactForm()
    else:
        form = ContactForm()
    # getting contacts based on filter
    filter = request.GET.get("filter")
    contacts = Contact.objects.filter(owner=request.user)
    if filter:
        contacts = contacts.filter(
            Q(name__icontains=filter) | Q(email__icontains=filter)
        )
    context = {"contact_form": form, "contacts": contacts, "filter": filter}
    return render(request, "home.html", context)


@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("/")
    return render(request, "home.html", {"contact": contact})


@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        # adding contact pk for exclude in ContactForm clean() override
        form = ContactForm(request.POST, instance=contact, pk=pk)
        form.owner = request.user
        if form.is_valid():
            contact.save()
            form = ContactForm()
            return redirect("/")
    else:
        # using instance property to populate form w/ retrieved data from Contact model
        form = ContactForm(instance=contact)
    contacts = Contact.objects.filter(owner=request.user)
    # pk added to context so we can access it in the template
    context = {"contact_form": form, "contacts": contacts, "pk": pk}
    return render(request, "home.html", context)


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class Login(LoginView):
    template_name = "registration/login.html"

    # redirect a user to the home page if they're already logged in
    def get(self, request, *args, **kwargs):
        self.object = None
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("/")


# as per docs, must add a custom creation form since we're using a custom User model
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": ("Username")})
        self.fields["password1"].widget.attrs.update({"placeholder": ("Password")})
        self.fields["password2"].widget.attrs.update({"placeholder": ("Confirm")})

    class Meta(UserCreationForm.Meta):
        model = User


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # redirect a user to the home page if they're already signed up
    def get(self, request, *args, **kwargs):
        self.object = None
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("/")


@login_required
def logout_view(request):
    logout(request)
    return redirect("/registration/login")


def check_username(request):
    username = request.POST.get("username")
    if not username:
        return HttpResponse("<span></span>")
    if get_user_model().objects.filter(username=username):
        return HttpResponse(
            '<span class="username--exists">This username already exists</span>'
        )
    else:
        return HttpResponse(
            '<span class="username--available">This username is available</span>'
        )
