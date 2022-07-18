from django.test import TestCase
from ..models import User, Contact


class HomeViewTests(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        self.john = User.objects.create_user(**self.credentials)
        # log in user
        self.client.post("/registration/login/", self.credentials, follow=True)
        Contact.objects.create(
            owner=self.john,
            name="Jim Doe",
            email="jim@test.com",
            phone="123-123-1233",
            contact_type="Professional",
        )

    def test_form_post(self):
        self.contact_info = {
            "name": "Jane Doe",
            "email": "jane@gmail.com",
            "phone_0": "415-394-3948",
            "contact_type": "Personal",
        }
        self.client.post("/", self.contact_info)
        jane = Contact.objects.filter(name="Jane Doe").count()
        self.assertEqual(jane, 1)

    def test_filter(self):
        response = self.client.get("?filter=jim")
        contacts = response.context["contacts"].count()
        self.assertEqual(contacts, 1)

    def test_delete(self):
        jim = Contact.objects.filter(name="Jim Doe").first()
        response = self.client.post(f"/delete/{jim.pk}")
        self.assertEqual(response.status_code, 302)
        jim = Contact.objects.filter(name="Jim Doe").exists()
        # checking for deletion
        self.assertFalse(jim)

    def test_delete_get(self):
        jim = Contact.objects.filter(name="Jim Doe").first()
        response = self.client.get(f"/delete/{jim.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home.html")

    def test_edit(self):
        jim = Contact.objects.filter(name="Jim Doe").first()
        response = self.client.post(f"/edit/{jim.pk}")
        self.assertTemplateUsed(response, template_name="home.html")
