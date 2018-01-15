from django import forms
from django_file_form.forms import UploadedFileField
from core.mixins import CustomFileFormMixin

from tinymce.widgets import TinyMCE

from projects.models import Project


class ProjectModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a form for the Project model."""

    image = UploadedFileField(label='Світлина', required=False)

    def __init__(self, *args, **kwargs):
        super(ProjectModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image

    class Meta:
        model = Project
        fields = ('title', 'short_descr', 'description',
                  'curators', 'slug', 'image')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 10}),
        }

    def save(self, commit=True):
        instance = super(ProjectModelForm, self)\
                .save(commit=False)
        image = self.cleaned_data['image']
        instance.image = image
        if commit:
            instance.save()

        self.delete_temporary_files()
        return instance
