from django import forms
from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin
from authors.models import Author


class AuthorModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render an Author model form."""

    image = UploadedFileField(label='Світлина', required=False)

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'about_author',
                  'image', 'tags', 'slug')
