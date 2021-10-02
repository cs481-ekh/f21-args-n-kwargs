from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse

from accounts.forms import AccountCreationForm


class TestViews(SimpleTestCase):

    def test_accounts_login_is_resolved(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_accounts_logout_is_resolved(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_accounts_dashboard_is_resolved(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class AccountFormTest(TestCase):
    def test_account_form_email_field_label(self):
        form = AccountCreationForm()
        self.assertTrue(form.fields['email'].label == 'Email')

    def test_account_form_password1_field_label(self):
        form = AccountCreationForm()
        self.assertTrue(form.fields['password1'].label == 'Password')

    def test_account_form_password2_field_label(self):
        form = AccountCreationForm()
        self.assertTrue(form.fields['password2'].label == 'Password confirmation')

    def test_account_form_valid_email(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password, 'password2' : password})
        self.assertTrue(form.is_valid())

    def test_account_form_invalid_root_email(self):
        email = "django@dev"
        password = "djangoIsAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password, 'password2' : password})
        self.assertFalse(form.is_valid())

    def test_account_form_invalid_base_email(self):
        email = "@dev.com"
        password = "djangoIsAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password, 'password2' : password})
        self.assertFalse(form.is_valid())

    def test_account_form_invalid_no_password1(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': '', 'password2' : password})
        self.assertFalse(form.is_valid())

    def test_account_form_invalid_no_password2(self):
        email = "django@dev.com"
        password = "djangoIsAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password, 'password2' : ''})
        self.assertFalse(form.is_valid())

    def test_account_form_invalid_diff_passwords(self):
        email = "django@dev.com"
        password1 = "djangoIsAwesome"
        password2 = "djangoIsNotAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password1, 'password2' : password2})
        self.assertFalse(form.is_valid())

    def test_account_form_invalid_diff_passwords(self):
        email = "django@dev.com"
        password1 = "djangoIsAwesome"
        password2 = "djangoIsNotAwesome"
        form = AccountCreationForm(data={'email': email, 'password1': password1, 'password2' : password2})
        self.assertFalse(form.is_valid())


