from django import forms
from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin
from books.models import Book


class BookModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a Book model form."""

    image = UploadedFileField(label='Світлина', required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(BookModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ('title', 'short_descr', 'description',
                  'from_author', 'image', 'price', 'in_stock',
                  'pages', 'cover', 'weight', 'height', 'length',
                  'depth', 'publisher', 'isbn_13', 'isbn_10',
                  'authors', 'tags', 'slug')
