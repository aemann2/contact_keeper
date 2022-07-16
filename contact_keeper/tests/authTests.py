from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import User


class LogInPageTests(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post(
            "/registration/login/", self.credentials, follow=True
        )
        # testing login
        self.assertTrue(response.context["user"].is_active)

    def test_bad_login(self):
        self.credentials = {"username": "jdoe", "password": "1234"}
        # send login data
        response = self.client.post(
            "/registration/login/", self.credentials, follow=True
        )
        # testing login
        self.assertFalse(response.context["user"].is_active)

    def test_logged_in_redirect_from_signup(self):
        # send login data
        self.client.post("/registration/login/", self.credentials, follow=True)
        response = self.client.get("/registration/signup/")
        # redirecting user from signup if logged in
        self.assertEqual(response.status_code, 302)

    def test_logged_in_redirect_from_login(self):
        # send login data
        self.client.post("/registration/login/", self.credentials, follow=True)
        response = self.client.get("/registration/login/")
        # redirecting user from signup if logged in
        self.assertEqual(response.status_code, 302)

    def test_branching(self):
        response = self.client.get("/registration/login/")
        self.assertTrue(response.context["user"].is_anonymous)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/login.html")


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = "testuser"
        self.email = "testuser@email.com"
        self.password = "Pass123?"

    def test_signup_page_url(self):
        response = self.client.get("/registration/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/signup.html")

    def test_signup_page_view_name(self):
        response = self.client.get("/registration/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            "/registration/signup/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
            },
        )
        # checking for redirect
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)


class LogoutTests(TestCase):
    def setUp(self):
        self.credentials = {"username": "jdoe", "password": "12345678"}
        User.objects.create_user(**self.credentials)
        self.client.post("/registration/login/", self.credentials, follow=True)

    def test_logout(self):
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 302)
