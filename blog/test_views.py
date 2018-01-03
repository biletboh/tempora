from django.test import TestCase


from unittest.mock import patch, MagicMock

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File
from django.conf import settings

from blog.models import Post
from blog.forms import PostForm


class PostListTestCase(TestCase):
    """
    Test Post List page.
    """

    def setUp(self):
        file_mock = MagicMock(spec=File)
        post1 = Post.objects.create(
                                title='test post',
                                body='body of the test post',
                                )
        post2 = Post.objects.create(
                                title='test post 2',
                                body='body of the test post 2',
                                )

    def test_status_code(self):
        url = reverse('blog:blog')
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_context(self):
        url = reverse('blog:blog')
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertTrue('posts' in resp.context)
        self.assertEqual(
                len([post.pk for post in resp.context['posts']]), 2)

    def test_template(self):
        url = reverse('blog:blog')
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url, follow=True)
        self.assertTemplateUsed(resp, 'blog/blog.html')


class PageTestCase(TestCase):
    """
    Test Post page.
    """

    def setUp(self):
        file_mock = MagicMock(spec=File)
        post1 = Post.objects.create(
                                title='test post',
                                body='body of the test post',
                                )

    def test_status_code(self):
        url = reverse('blog:page', kwargs={'pk':1})
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_context(self):
        url = reverse('blog:page', kwargs={'pk':1})
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url)
        self.assertTrue('object' in resp.context)
        self.assertEqual(resp.context['object'], Post.objects.all()[0])

    def test_template(self):
        url = reverse('blog:page', kwargs={'pk':1})
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'en'})
        resp = self.client.get(url)
        self.assertTemplateUsed(resp, 'blog/page.html')

