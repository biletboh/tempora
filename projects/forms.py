from django import forms
from django_file_form.forms import UploadedFileField
from core.mixins import CustomFileFormMixin

from projects.models import Project


class ProjectModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a project model form."""

    image = UploadedFileField(label='Світлина', required=False)

    class Meta:
        model = Project
        fields = ('title', 'short_descr', 'description',
                  'curators', 'slug', 'image')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

