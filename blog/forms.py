from django import forms
from django_file_form.forms import UploadedFileField
from tinymce.widgets import TinyMCE

from core.mixins import CustomFileFormMixin
from blog.models import Post


class PostModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a Post model form."""

    image = UploadedFileField(label='Світлина', required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('title', 'body', 'short_descr', 'slug')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 50}),
        }

    def save(self, commit=True):
        instance = super(PostModelForm, self)\
                .save(commit=False)
        instance.user = self.user

        if commit:
            instance.save()
        return instance
