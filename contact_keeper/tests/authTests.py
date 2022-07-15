from django.test import TestCase
from ..models import User


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post(
            "/registration/login/", self.credentials, follow=True
        )
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
