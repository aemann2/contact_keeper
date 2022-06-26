from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class Profile(TemplateView):
    template_name = "accounts/profile.html"


class Login(LoginView):
    template_name = "registration/login.html"
