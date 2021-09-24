from django.test import SimpleTestCase
from django.urls import reverse


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
