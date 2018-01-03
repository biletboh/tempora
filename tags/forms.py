from django import forms
from form_utils import forms as betterforms


class TagForm(betterforms.BetterForm):
    title = forms.CharField(label="Назва", max_length=40)
    description = forms.CharField(label="Опис", max_length=100)

    class Meta:
        fieldsets = [
                ('main', {'fields': ['title',], 'legend': 'main', }),
                ('text-area', {'fields': ['description'], 'legend': 'text-area'}),
                ]

