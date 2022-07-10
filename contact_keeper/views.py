from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm


@login_required
def home(request):
    if request.POST:
        # create form instance POST data, validate, attach user, and save
        form = ContactForm(request.POST)
        if form.is_valid():
            form.owner = request.user
            form.save()
            # reset form
            form = ContactForm()
    else:
        form = ContactForm()
    all_contacts = Contact.objects.filter(owner=request.user)
    context = {"contact_form": form, "contacts": all_contacts}
    return render(request, "home.html", context)


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.POST:
        contact.delete()
        return redirect("/")
    return render(request, "home.html", {"contact": contact})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact.save()
            form = ContactForm()
            return redirect("/")
    else:
        # using instance property to populate form w/ retrieved data from Contact model
        form = ContactForm(instance=contact)
    all_contacts = Contact.objects.filter(owner=request.user)
    # pk added to context so we can access it in the template
    context = {"contact_form": form, "contacts": all_contacts, "pk": pk}
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


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # redirect a user to the home page if they're already signed up
    def get(self, request, *args, **kwargs):
        self.object = None
        if request.user.is_anonymous:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/registration/login")
