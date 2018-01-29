from django import forms

from ajax_select import make_ajax_field
from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin
from books.models import Book


class BookModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a Book model form."""

    image = UploadedFileField(label='Світлина', required=False)
    authors = make_ajax_field(Book, 'authors', 'authors', help_text=None,
                              plugin_options={'minLength': 2})
    tags = make_ajax_field(Book, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})

    def __init__(self, *args, **kwargs):
        super(BookModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
        self.fields['publisher'].initial = 'Темпора'

    class Meta:
        model = Book
        fields = ('title', 'short_descr', 'description',
                  'from_author', 'image', 'price', 'in_stock',
                  'pages', 'cover', 'weight', 'height', 'length',
                  'depth', 'publisher', 'isbn_13', 'isbn_10',
                  'authors', 'tags', 'slug')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'from_author': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 12}),
        }
