from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import ContactForm


@login_required
def home(request):
    if request.POST:
        print("here")
    context = {"contact_form": ContactForm}
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