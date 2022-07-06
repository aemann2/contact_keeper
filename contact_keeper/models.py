from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phone_field import PhoneField
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)


class CustomPhoneField(PhoneField):
    # overwriting validation error for PhoneField
    @staticmethod
    def _validate_E164(value):
        if value and not value.is_E164:
            raise ValidationError("E164 error: Please enter a valid phone number")


class Contact(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = CustomPhoneField(E164_only=True, max_length=15)
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
