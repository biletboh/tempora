from django.test import TestCase


class NotesListTestCase(TestCase):

    def test_landing(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'pbhouse/landing.html')

