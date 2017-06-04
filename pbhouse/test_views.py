from django.test import TestCase 
from django.core.urlresolvers import reverse 
from django.conf import settings


class LandingTestCase(TestCase):

    def test_status_code(self):
        url = reverse('pbhouse:landing') 
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_template(self):
        url = reverse('pbhouse:landing') 
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertTemplateUsed(resp, 'pbhouse/landing.html')

