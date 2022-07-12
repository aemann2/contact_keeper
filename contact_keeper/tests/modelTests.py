from django.test import TestCase
from ..models import User

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        User.objects.create(
            username="jdoe", email="john@gmail.com", password="12345678"
        )
        User.objects.create(
            username="testUser", email="test@test.com", password="87654321"
        )

    def test_user_registered(self):
        users = User.objects.all()
        john = User.objects.get(username="jdoe")
        self.assertEqual(users.count(), 2)
        self.assertEqual(john.username, "jdoe")
