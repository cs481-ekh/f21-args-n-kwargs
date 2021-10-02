from django.db import IntegrityError
from django.test import TestCase

from accounts.models import Account


class AccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Account.objects.create(email="python@dev.com", password="computerscience123")
        Account.objects.create_superuser(email="django@admin.com", password="Admin123456")

    def test_user_email_isUnique(self):
        with self.assertRaises(IntegrityError):
            Account.objects.create(email="python@dev.com", password="diffpasswordSameUserEmail")

    def test_user_no_email_label(self):
        with self.assertRaises(ValueError):
            Account.objects.create_superuser(email="", password="noemailfield")

    def test_user_email_label(self):
        account = Account.objects.get(id=1)
        email_label = account.email
        self.assertEqual(email_label, 'python@dev.com')

    def test_user_is_admin(self):
        account = Account.objects.get(id=1)
        admin_perms = account.is_admin
        self.assertEqual(admin_perms, False)

    def test_user_is_active(self):
        account = Account.objects.get(id=1)
        active_status = account.is_active
        self.assertEqual(active_status, True)

    def test_user_is_staff(self):
        account = Account.objects.get(id=1)
        staff_perms = account.is_staff
        self.assertEqual(staff_perms, False)

    def test_user_is_superuser(self):
        account = Account.objects.get(id=1)
        superuser_perms = account.is_superuser
        self.assertEqual(superuser_perms, False)

    def test_superuser_email_label(self):
        account = Account.objects.get(id=2)
        field_label = account.email
        self.assertEqual(field_label, 'django@admin.com')

    def test_superuser_is_admin(self):
        account = Account.objects.get(id=2)
        admin_perms = account.is_admin
        self.assertEqual(admin_perms, True)

    def test_superuser_is_active(self):
        account = Account.objects.get(id=2)
        active_status = account.is_active
        self.assertEqual(active_status, True)

    def test_superuser_is_staff(self):
        account = Account.objects.get(id=2)
        staff_perms = account.is_staff
        self.assertEqual(staff_perms, True)

    def test_superuser_is_superuser(self):
        account = Account.objects.get(id=2)
        superuser_perms = account.is_superuser
        self.assertEqual(superuser_perms, True)
