from django.test import TestCase
from ..models import User

class LogInPageTests(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        User.objects.create_user(**self.credentials)
        # log in user
        self.client.post(
            "/registration/login/", self.credentials, follow=True
        )
    
    def test_filter(self):
        response = self.client.get("?filter=test")