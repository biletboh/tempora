from django import forms

from ajax_select import make_ajax_field

from core.mixins import SlugCleanMixin
from video.models import Video


class VideoModelForm(SlugCleanMixin, forms.ModelForm):
    """Render a Video model form."""

    tags = make_ajax_field(Video, 'tags', 'tags', help_text=None,
                           plugin_options={'minLength': 2})

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Video
        fields = ('title', 'short_descr', 'slug', 'selected', 'user',
                  'youtube')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }

    def save(self):
        instance = super().save(commit=False)
        print('hi')
        if self.cleaned_data['user']:
            instance.user = self.cleaned_data['user']
        else:
            instance.user = self.user

        instance.save()
        return instance

    def get_slug_fields(self):
        return ['title']
