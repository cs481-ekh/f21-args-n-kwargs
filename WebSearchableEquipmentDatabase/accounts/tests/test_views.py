from http import HTTPStatus
from django.test import TestCase
from accounts.models import Account


class RegisterAccountViewTest(TestCase):
    def test_register_endpoint(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_register_success(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        response = self.client.post("/register/", data={'email': email, 'password1': password, 'password2': password})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_register_failure(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        response = self.client.post("/register/",
                                    data={'email': email, 'password1': password, 'password2': 'differentpassword'})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_register_user_perms(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        self.client.post("/register/", data={'email': email, 'password1': password, 'password2': password})
        user = Account.objects.get(email=email)
        self.assertEqual(user.is_active, False)

