from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phone_field import PhoneField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


class Contact(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField(E164_only=True)
    PERSONAL = "Personal"
    PROFESSIONAL = "Professional"
    CONTACT_TYPE_CHOICES = [
        (PERSONAL, "Personal"),
        (PROFESSIONAL, "Professional"),
    ]
    contact_type = models.CharField(
        max_length=12,
        choices=CONTACT_TYPE_CHOICES,
        default=PROFESSIONAL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
