from django import forms
from django.utils import timezone

from ajax_select import make_ajax_field
from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin, SlugCleanMixin
from books.models import Book, Order


class BookModelForm(CustomFileFormMixin, SlugCleanMixin, forms.ModelForm):
    """Render a Book model form."""

    image = UploadedFileField(label='Світлина', required=False)
    authors = make_ajax_field(Book, 'authors', 'authors', help_text=None,
                              plugin_options={'minLength': 2})
    tags = make_ajax_field(Book, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
        self.fields['publisher'].initial = 'Темпора'
        self.fields['pub_date'].input_formats = ['%Y-%m-%d %H:%M']
        self.fields['pub_date'].widget = forms.TextInput()
        if not self.instance.pub_date:
            self.fields['pub_date'].initial = timezone.now().strftime(
                '%Y-%m-%d %H:%M')

    class Meta:
        model = Book
        fields = ('title', 'short_descr', 'description',
                  'from_author', 'image', 'price', 'in_stock',
                  'pages', 'cover', 'height', 'length', 'weight',
                  'publisher', 'isbn_13', 'authors', 'tags', 'slug',
                  'pub_year', 'pub_date', 'release', 'selected',
                  'new', 'best_seller', 'translators')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'from_author': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 12}),
        }

    def get_slug_fields(self):
        return ['title']


class OrderModelForm(forms.ModelForm):
    """Render a book order model form."""

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'message', 'quantity', 'book')
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
            'book': forms.NumberInput()
        }
