from django.contrib import admin
from django.urls import path
from contact_keeper.views import Login, SignUp, home, delete_contact, edit_contact, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("registration/login/", Login.as_view(), name="login"),
    path("registration/signup/", SignUp.as_view(), name="signup"),
    path("logout", logout_view, name="logout"),
    path("delete/<int:pk>", delete_contact, name='delete_contact'),
    path("edit/<int:pk>", edit_contact, name='edit_contact')
]

"""src URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
