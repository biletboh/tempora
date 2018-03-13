from django import forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    """Render Custom SignupForm."""

    fn_attrs = {'placeholder': _('Ім’я')}
    ln_attrs = {'placeholder': _('Прізвище')}
    first_name = forms.CharField(
                            max_length=40, label=_('Ім’я'),
                            widget=forms.TextInput(attrs=fn_attrs))
    last_name = forms.CharField(
                            max_length=40, label=_('Прізвище'),
                            widget=forms.TextInput(attrs=ln_attrs))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
