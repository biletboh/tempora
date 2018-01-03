from django.conf import settings
from django.shortcuts import resolve_url

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    """Customize auth processing."""

    def get_login_redirect_url(self, request):
        """Redirect superusers and affiliates to user list in admin panel."""

        url = settings.LOGIN_REDIRECT_URL
        print(resolve_url(url))
        return resolve_url(url)
