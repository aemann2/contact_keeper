from django.test import TestCase
from ..models import User
from ..models import Contact
from django.core.exceptions import ValidationError

# Create your tests here.
class UserAndContactTests(TestCase):
    def setUp(self):
        self.john = User.objects.create(
            username="jdoe", email="john@gmail.com", password="12345678"
        )
        self.testUser = User.objects.create(
            username="testUser", email="test@test.com", password="87654321"
        )

        self.jane = Contact.objects.create(
            owner=self.john,
            name="Jane Doe",
            email="jane@gmail.com",
            phone="555-555-5555",
            contact_type="Personal",
        )
        self.jim = Contact.objects.create(
            owner=self.john,
            name="Jim Doe",
            email="jim@test.com",
            phone="123-123-1233",
            contact_type="Professional",
        )

    def test_user_registered(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 2)
        self.assertEqual(self.john.username, "jdoe")

    def test_contact_created_with_owner(self):
        contacts = Contact.objects.all()
        self.assertEqual(contacts.count(), 2)
        self.assertEqual(self.jane.name, "Jane Doe")
        self.assertEqual(self.jane.owner.username, "jdoe")

    def test_contact_str_method(self):
        self.assertEqual(str(self.jane), "Jane Doe")

    def test_validate_E164(self):
        with self.assertRaises(ValidationError):
            self.jim.full_clean()

    def test_contact_delete(self):
        Contact.objects.filter(email=self.jane.email).delete()
        contacts = Contact.objects.count()
        self.assertEqual(contacts, 1)
