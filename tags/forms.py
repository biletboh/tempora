from django import forms

from tags.models import Tag


class TagModelForm(forms.ModelForm):
    """Render a Tag model form."""

    class Meta:
        model = Tag
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
