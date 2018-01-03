from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django_file_form.forms import FileFormMixin
from django import forms


class IsSuperUserTestMixin(LoginRequiredMixin, UserPassesTestMixin, object):
    """Check if a user is loged in and is a superuser."""

    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = 'У вас немає прав переглядати цю сторінку.'
            messages.warning(self.request, denied)
        return user


class CustomFileFormMixin(FileFormMixin):
    form_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    upload_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    delete_url = forms.CharField(widget=forms.HiddenInput(), required=False)

