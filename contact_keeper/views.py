from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class Login(LoginView):
    template_name = "registration/login.html"


def logout_view(request):
    logout(request)
    return redirect("/")
