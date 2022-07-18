from ..forms import ContactForm
from django.test import TestCase
from ..models import User
from django.core.exceptions import ValidationError


class FormTests(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        self.john = User.objects.create_user(**self.credentials)
        # log in user
        self.client.post("/registration/login/", self.credentials, follow=True)
        self.form_with_owner = ContactForm
        ContactForm.owner = self.john

    def test_form_valid(self):
        form_data = {
            "name": "Jane Doe",
            "email": "jane@gmail.com",
            "phone_0": "415-394-3948",
            "contact_type": "Personal",
        }
        form = self.form_with_owner(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            "name": "Jane Doe",
            "email": "jane@gmail.com",
            "contact_type": "Personal",
        }
        form = self.form_with_owner(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["phone"][0], "This field is required.")

    def test_duplicate_invalid(self):
        form_data = {
            "name": "Jane Doe",
            "email": "jane@gmail.com",
            "phone_0": "415-394-3948",
            "contact_type": "Personal",
        }
        form = self.form_with_owner(data=form_data)
        form.save()
        # creating a form w/ duplicate data and checking if valid
        form = self.form_with_owner(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)
