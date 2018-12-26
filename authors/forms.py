from django import forms

from ajax_select import make_ajax_field
from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin, SlugCleanMixin

from authors.models import Author


class AuthorModelForm(CustomFileFormMixin, SlugCleanMixin, forms.ModelForm):
    """Render an Author model form."""

    image = UploadedFileField(label='Світлина', required=False)
    tags = make_ajax_field(Author, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'about_author',
                  'image', 'tags', 'slug')

    def get_slug_fields(self):
        return ['first_name', 'last_name']
