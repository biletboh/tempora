from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin
from users.models import UserProfile


class BaseUserModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render User model form."""

    avatar = UploadedFileField(label='Світлина', required=False)

    def __init__(self, *args, **kwargs):
        super(BaseUserModelForm, self).__init__(*args, **kwargs)

        # set an intial image
        if self.instance:
            self.fields['avatar'].initial = self.instance.avatar

    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'position', 'info',
                  'facebook', 'twitter', 'linkedin', 'goodreads')
        widgets = {
            'info': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class AccountUserModelForm(BaseUserModelForm):

    def save(self, commit=True):
        instance = super(AccountUserModelForm, self)\
                .save(commit=False)

        # set user profile image
        avatar = self.cleaned_data['avatar']
        instance.avatar = avatar

        if commit:
            instance.save()
            self.delete_temporary_files()

        return instance


class UserModelForm(BaseUserModelForm):
    """Render Admin User model form."""

    team = forms.BooleanField(label=_('Співробітник(ця)'), required=False,
                              initial=False)
    author = forms.BooleanField(label=_('Автор(к)а'), required=False,
                                initial=False)
    blogger = forms.BooleanField(label=_('Блогер(ка)'), required=False,
                                 initial=False)

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)

        # user groups
        self.team = Group.objects.get(name='Team')
        self.authors = Group.objects.get(name='Authors')
        self.bloggers = Group.objects.get(name='Bloggers')

        if self.instance.id:
            in_team = self.instance.groups.filter(name='Team').exists()
            in_authors = self.instance.groups.filter(name='Authors').exists()
            in_bloggers = self.instance.groups.filter(name='Bloggers').exists()
            self.fields['team'].initial = in_team
            self.fields['author'].initial = in_authors
            self.fields['blogger'].initial = in_bloggers

    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'position', 'info',
                  'is_staff', 'is_active', 'facebook', 'twitter', 'linkedin',
                  'goodreads')
        widgets = {
            'info': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def save(self, commit=True):
        instance = super(UserModelForm, self)\
                .save(commit=True)

        # set user profile image
        avatar = self.cleaned_data['avatar']
        instance.avatar = avatar

        # set user groups
        team = self.cleaned_data['team']
        author = self.cleaned_data['author']
        blogger = self.cleaned_data['blogger']

        if team:
            instance.groups.add(self.team)
        if author:
            instance.groups.add(self.authors)
        if blogger:
            instance.groups.add(self.bloggers)

        if commit:
            instance.save()
            self.delete_temporary_files()

        return instance
