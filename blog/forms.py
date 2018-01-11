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
        if self.instance:
            self.fields['image'].initial = self.instance.image

    class Meta:
        model = Post
        fields = ('title', 'body', 'short_descr', 'slug')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self, commit=True):
        instance = super(PostModelForm, self)\
                .save(commit=False)
        instance.user = self.user
        image = self.cleaned_data['image']
        instance.image = image
        if commit:
            instance.save()

        self.delete_temporary_files()
        return instance
