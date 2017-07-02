from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django_file_form.forms import FileFormMixin, UploadedFileField
from form_utils import forms as betterforms
from allauth.account.forms import PasswordVerificationMixin, PasswordField

from users.models import UserProfile


class BaseUserProfileForm(FileFormMixin, betterforms.BetterForm):
    """
    Provide Base Form for UserProfile.
    """

    email = forms.CharField(label=_('Емейл'), max_length=100)
    first_name = forms.CharField(label=_("Ім'я"), max_length=80)
    last_name = forms.CharField(label=_('Прізвище'), max_length=80)
    info = forms.CharField(
                        label=_('Розкажіть про себе'), max_length=256,
                        widget=forms.Textarea,
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
    goodreads = forms.CharField(
                            label=_('Goodreads'), max_length=200,
                            required=False,)
    avatar = UploadedFileField(label=_('Світлина'), required=False)
    form_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    upload_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    delete_url = forms.CharField(widget=forms.HiddenInput(), required=False)

 
    def clean_password2(self):
        cleaned_data = super(BaseUserProfileForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if (password1 and password2) and password1 != password2:
            self.add_error(
                'password2', _("You must type the same password each time.")
            )
        return password2 


class UserManagementForm(BaseUserProfileForm):
    """
    Provide Form for creation of users with password required field.
    """
    
    is_staff = forms.BooleanField(
                                label=_('Редактор(ка)'), required=False, 
                                initial=False)
    is_active = forms.BooleanField(
                                label=_('Активний'), required=False,
                                initial=False)
    team = forms.BooleanField(
                            label=_('Співробітник(ця)'), required=False,
                                initial=False)
    authors = forms.BooleanField(
                            label=_('Автор(к)а'), required=False,
                            initial=False)
    bloggers = forms.BooleanField(
                            label=_('Блогер(ка)'), required=False,
                            initial=False)
    
    class Meta:
        fieldsets = [
                ('main', {'fields': [
                                'email', 'last_name', 'first_name', 'info',
                                'facebook', 'twitter', 'linkedin', 
                                'goodreads',
                                ], 'legend': 'main', }),
                ('privileges', {'fields': [
                                        'is_staff', 'is_active', 'team',
                                        'authors', 'bloggers'
                                        ], 'legend': 'privileges', }),
                ('password', {
                            'fields': ['password1', 'password2'],
                            'legend': 'password', }),
                ('avatar', {'fields': [
                                    'avatar', 'form_id', 'upload_url',
                                    'delete_url'
                                    ], 'legend': 'password', }),
                ]


class UserCreateForm(UserManagementForm):
    """
    Provide Form for creation of users with password required field.
    """
    
    password1 = PasswordField(label=_('Пароль'), required=True)
    password2 = PasswordField(label=_('Пароль (знову)'), required=True)
    
    class Meta:
        fieldsets = [
                ('main', {'fields': [
                                'email', 'last_name', 'first_name', 'info',
                                'facebook', 'twitter', 'linkedin', 
                                'goodreads',
                                ], 'legend': 'main', }),
                ('privileges', {'fields': [
                                        'is_staff', 'is_active', 'team',
                                        'authors', 'bloggers'
                                        ], 'legend': 'privileges', }),
                ('password', {
                            'fields': ['password1', 'password2'],
                            'legend': 'password', }),
                ('avatar', {'fields': [
                                    'avatar', 'upload_url',
                                    'form_id', 'delete_url'
                                    ], 'legend': 'password', }),
                ]


class UserUpdateForm(UserManagementForm):
    """
    Provide Form for user update with optional password update.
    """
    
    password1 = PasswordField(label=_('Пароль'), required=False)
    password2 = PasswordField(label=_('Пароль (знову)'), required=False)


class ProfileUpdateForm(BaseUserProfileForm):
    """
    Provide Form for profile information update 
    with optional password update.
    """
    
    password1 = PasswordField(label=_('Пароль'), required=False)
    password2 = PasswordField(label=_('Пароль (знову)'), required=False)

    class Meta:
        fieldsets = [
                ('main', {'fields': [
                                'email', 'last_name', 'first_name', 'info',
                                'facebook', 'twitter', 'linkedin',
                                'goodreads',
                                ], 'legend': 'main', }),
                ('password', {
                            'fields': ['password1', 'password2'],
                            'legend': 'password', }),
                ('avatar', {'fields': [
                                    'avatar', 'form_id', 'upload_url',
                                    'delete_url'
                                    ], 'legend': 'password', }),
                ]

