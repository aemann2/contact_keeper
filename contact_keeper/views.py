from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class Login(LoginView):
    template_name = "registration/login.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def logout_view(request):
    logout(request)
    return redirect("/")
