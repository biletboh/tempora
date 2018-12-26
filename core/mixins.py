from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ImproperlyConfigured
from django import forms

from django_file_form.forms import FileFormMixin
from transliterate import slugify


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


class SlugCleanMixin:
    """Check uniqueness of the slug field input in forms."""

    def get_slug_fields(self):
        """Overwrite get_slug_fields to specify fields to slugify."""

        return None

    def slugify_fields(self):
        """Slugify fields based on fields_to_slugify attribute
        on Meta class."""

        fields_to_slugify = self.get_slug_fields()

        if not fields_to_slugify:
            raise ImproperlyConfigured(
                'Provide the get_slug_fields method that returns a list '
                + 'of values for fields to slugify')

        for idx, field in enumerate(fields_to_slugify):
            if idx == 0:
                slug = slugify(self.cleaned_data[field])
            else:
                slug = slug + '-' + slugify(self.cleaned_data[field])
        return slug

    def clean_slug(self):
        """Clean a slug field and check for the uniqueness."""

        slug_data = self.cleaned_data['slug']

        if slug_data:
            slug = slug_data
        else:
            slug = self.slugify_fields()

        try:
            self.Meta.model.objects.get(slug=slug)
            error_text = ('Запис з таким посиланням уже існує. '
                          + 'Оновіть посилання.')
            self.data = self.data.copy()
            self.data['slug'] = slug
            raise forms.ValidationError(error_text)
        except self.Meta.model.DoesNotExist:
            return slug
