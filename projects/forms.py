from django import forms

from ajax_select import make_ajax_field
from django_file_form.forms import UploadedFileField
from tinymce.widgets import TinyMCE

from core.mixins import CustomFileFormMixin, SlugCleanMixin
from projects.models import Project
from tags.models import Tag


class ProjectModelForm(CustomFileFormMixin, SlugCleanMixin, forms.ModelForm):
    """Render a form for the Project model."""

    image = UploadedFileField(label='Світлина', required=False)
    icon_image = UploadedFileField(label='Іконка', required=False)
    curators = make_ajax_field(Project, 'curators', 'curators', help_text=None,
                               plugin_options={'minLength': 2})
    tags = make_ajax_field(Project, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})
    project_tag = make_ajax_field(Project, 'project_tag', 'tags',
                                  help_text=None,
                                  plugin_options={'minLength': 2},
                                  required=False)
    project_tag_new = forms.CharField(max_length=100, required=False,
                                      widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(ProjectModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
            self.fields['icon_image'].initial = self.instance.icon_image
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
        instance = super().save()

        new_tag = self.cleaned_data['project_tag_new']
        try:
            Tag.objects.get(title=new_tag)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(title=new_tag)
            instance.project_tag = tag

        image = self.cleaned_data['image']
        icon_image = self.cleaned_data['icon_image']
        instance.image = image
        instance.icon_image = icon_image
        instance.save()
        self.delete_temporary_files()
        return instance

    def get_slug_fields(self):
        return ['title']
