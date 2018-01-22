from django import forms
from django_file_form.forms import UploadedFileField
from core.mixins import CustomFileFormMixin

from ajax_select import make_ajax_field
from tinymce.widgets import TinyMCE

from projects.models import Project


class ProjectModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a form for the Project model."""

    image = UploadedFileField(label='Світлина', required=False)
    curators = make_ajax_field(Project, 'curators', 'curators', help_text=None,
                               plugin_options={'minLength': 2})
    tags = make_ajax_field(Project, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})
    project_tag = make_ajax_field(Project, 'project_tag', 'tags',
                                  help_text=None,
                                  plugin_options={'minLength': 2})

    def __init__(self, *args, **kwargs):
        super(ProjectModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
            self.fields['tags'].label = 'Теги'
            self.fields['project_tag'].label = 'Тег проекту'
            self.fields['curators'].label = 'Куратори'

    class Meta:
        model = Project
        fields = ('title', 'short_descr', 'description', 'curators', 'slug',
                  'image', 'tags', 'project_tag')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 10}),
        }

    def save(self):
        instance = super(ProjectModelForm, self).save()
        image = self.cleaned_data['image']
        instance.image = image
        instance.save()
        self.delete_temporary_files()
        return instance
