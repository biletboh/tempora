from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from form_utils import forms as betterforms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget 
from datetimewidget.widgets import DateWidget

from users.models import UserProfile


class SignupForm(forms.Form):
    """
    Render Custom SignupForm.
    """

    first_name = forms.CharField(max_length=40, label=_('First Name'))
    last_name = forms.CharField(max_length=40, label=_('Last Name'))
#    info = forms.CharField(label=_('Tell about yourself'), max_length=200)
#    facebook = forms.CharField(label=_('Facebook'), max_length=200)
#    twitter = forms.CharField(label=_('Twitter'), max_length=200)
#    linkedin = forms.CharField(label=_('Linkedin'), max_length=200)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
#        user.info = self.cleaned_data['info']
#        user.facebook = self.cleaned_data['facebook']
#        user.twitter = self.cleaned_data['twitter']
#        user.linkedin = self.cleaned_data['linkedin']
        user.save()

