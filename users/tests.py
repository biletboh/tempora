from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings


class DashboardTestCase(TestCase):
    """
    Test Dashboard routing.
    """

    def test_status_code(self):
        url = reverse('users:dashboard') 
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_template(self):
        url = reverse('users:dashboard') 
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertTemplateUsed(resp, 'users/index.html')

