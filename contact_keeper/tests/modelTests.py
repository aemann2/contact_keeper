from django.test import TestCase
from ..models import User
from ..models import Contact

# Create your tests here.
class UserAndContactTests(TestCase):
    def setUp(self):
        User.objects.create(
            username="jdoe", email="john@gmail.com", password="12345678"
        )
        User.objects.create(
            username="testUser", email="test@test.com", password="87654321"
        )

        john = User.objects.get(username="jdoe")
        Contact.objects.create(
            owner=john,
            name="Jane Doe",
            email="jane@gmail.com",
            phone="555-555-5555",
            contact_type="Personal",
        )
        Contact.objects.create(
            owner=john,
            name="Jim Doe",
            email="jim@test.com",
            phone="415-555-5555",
            contact_type="Professional",
        )

    def test_user_registered(self):
        users = User.objects.all()
        john = User.objects.get(username="jdoe")
        self.assertEqual(users.count(), 2)
        self.assertEqual(john.username, "jdoe")

    def test_contact_created_with_owner(self):
        jane = Contact.objects.get(email="jane@gmail.com")
        contacts = Contact.objects.all()
        self.assertEqual(contacts.count(), 2)
        self.assertEqual(jane.name, "Jane Doe")
        self.assertEqual(jane.owner.username, "jdoe")

    def test_contact_delete(self):
        jane = Contact.objects.get(email="jane@gmail.com")
        Contact.objects.filter(email=jane.email).delete()
        contacts = Contact.objects.count()
        self.assertEqual(contacts, 1)
