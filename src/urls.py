from django.contrib import admin
from django.urls import path
from contact_keeper.views import Home, Profile, Login, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("accounts/profile/", Profile.as_view(), name="profile"),
    path("accounts/login/", Login.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
]


"""src URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
