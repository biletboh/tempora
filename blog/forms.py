from django import forms

from ajax_select import make_ajax_field
from django_file_form.forms import UploadedFileField
from tinymce.widgets import TinyMCE

from core.mixins import CustomFileFormMixin, SlugCleanMixin
from blog.models import Post


class PostModelForm(CustomFileFormMixin, SlugCleanMixin, forms.ModelForm):
    """Render a Post model form."""

    image = UploadedFileField(label='Світлина', required=False)
    tags = make_ajax_field(Post, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image

    class Meta:
        model = Post
        fields = ('title', 'body', 'short_descr', 'slug', 'tags', 'selected')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self):
        instance = super().save(commit=False)
        image = self.cleaned_data['image']
        instance.image = image
        instance.user = self.user
        instance.save()
        self.delete_temporary_files()
        return instance

    def get_slug_fields(self):
        return ['title']
