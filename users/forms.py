from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from form_utils import forms as betterforms
from allauth.account.forms import PasswordVerificationMixin, PasswordField

from users.models import UserProfile


class BaseUserProfileForm(betterforms.BetterForm):
    """
    Provide Base Form for UserProfile.
    """

    email = forms.CharField(label=_('Email'), max_length=100)
    first_name = forms.CharField(label=_('First Name'), max_length=80)
    last_name = forms.CharField(label=_('Last Name'), max_length=80)
    info = forms.CharField(
                        label=_('Tell about yourself'), max_length=200,
                        required=False,)
    facebook = forms.CharField(
                            label=_('Facebook'), max_length=200,
                            required=False,)
    twitter = forms.CharField(
                            label=_('Twitter'), max_length=200,
                            required=False,)
    linkedin = forms.CharField(
                            label=_('Linkedin'), max_length=200,
                            required=False,)
    is_staff = forms.BooleanField(
                                label=_('Editor'), required=False, 
                                initial=False)
    is_active = forms.BooleanField(
                                label=_('Is Active'), required=False,
                                initial=False)
    
    def clean_password2(self):
        cleaned_data = super(BaseUserProfileForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if (password1 and password2) and password1 != password2:
            self.add_error(
                'password2', _("You must type the same password each time.")
            )
        return password2 


    class Meta:
        fieldsets = [
                ('main', {'fields': ['email', 'last_name', 'first_name', 'info', 'facebook', 'twitter', 'linkedin'], 'legend': 'main', }),
                ('privileges', {'fields': ['is_staff', 'is_active'], 'legend': 'privileges', }),
                ('password', {'fields': ['password1', 'password2'], 'legend': 'password', }),
                ]


class UserCreateForm(BaseUserProfileForm):
    """
    Provide Form for creation of users with password required field.
    """

    password1 = PasswordField(label=_('Password'), required=True)
    password2 = PasswordField(label=_('Password (again)'), required=True)

