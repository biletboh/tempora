from django import forms
from django_file_form.forms import FileFormMixin, UploadedFileField
from form_utils import forms as betterforms
from tinymce.widgets import TinyMCE
from django.forms.widgets import HiddenInput
from django.utils import timezone


class PostForm(FileFormMixin, betterforms.BetterForm):
    title = forms.CharField(label="name", max_length=200)
    body = forms.CharField(
                        label="body",
                        widget=TinyMCE(attrs={'cols': 80, 'rows': 50}), 
                        required=False)
    image = UploadedFileField(label="image", required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [
                ('main', {'fields': ['title',], 'legend': 'main', }),
                ('text-area', {'fields': ['body'], 'legend': 'text-area'}),
                ('images', {
                        'fields': [
                                    'image', 'form_id', 'upload_url', 
                                    'delete_url'],
                        'legend': 'images'}),
                ]

