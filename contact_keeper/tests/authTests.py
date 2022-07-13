from django.test import TestCase, Client
from ..models import User


class SimpleTest(TestCase):
    def setUp(self):
        User.objects.create(
            username="jdoe", email="john@gmail.com", password="12345678"
        )
        self.client = Client()

    def test_200(self):
        response = self.client.get("/registration/login/")
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        response = self.client.post(
            "/registration/login/", {"username": "jdoe", "password": "12345678"}
        )
        print(response)
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    # def test_login_fail(self):
    #     response = self.client.post(
    #         "/registration/login/", {"username": "jdoe", "password": "1234"}
    #     )
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
