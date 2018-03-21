from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import reverse

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    """Customize auth processing."""

    def get_login_redirect_url(self, request):
        """Redirect superusers and affiliates to user list in admin panel."""

        user = self.request.user
        url = settings.LOGIN_REDIRECT_URL

        if user.is_superuser:
            url = reverse('books:order_list')

        return resolve_url(url)

    def is_open_for_signup(self, request):
        """Close the website for a signup."""

        return False
