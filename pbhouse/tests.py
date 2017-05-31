from unittest.mock import patch

from django.test import TestCase
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class NotesListTestCase(TestCase):

    def test_landing(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'pbhouse/landing.html')


class UserProfileTestCase(TestCase):

    def test_signal(self):
        
        with patch(
            'pbhouse.signals.create_user_profile', 
            autospec=True) as mocked_handler:
            post_save.connect(mocked_handler, sender=User)

        with patch(
            'pbhouse.signals.save_user_profile', 
            autospec=True) as mocked_handler2:
            post_save.connect(mocked_handler2, sender=User)



        user = User.objects.create(
                                username='editor1', first_name='John', 
                                last_name='Doe', email='johndoe@gmail.com',
                                password='142fdasf3D')

        self.assertTrue(mocked_handler.call_count, 1) 
        self.assertTrue(mocked_handler2.call_count, 1) 

