from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField

from users.managers import UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Provide model for Custom User Profile with email registration.
    """

    email = models.EmailField('Емейл', unique=True)
    first_name = models.CharField("Ім'я", max_length=30)
    last_name = models.CharField('Прізвище', max_length=30)
    date_joined = models.DateTimeField('Дата', auto_now_add=True)
    avatar = ThumbnailerImageField('Світлина', upload_to='profile_images',
                                   blank=True)
    info = models.CharField('Iнформація', max_length=512, blank=True)
    facebook = models.CharField('Facebook', max_length=128, blank=True)
    twitter = models.CharField('Twitter', max_length=128, blank=True)
    linkedin = models.CharField('Linkedin', max_length=128, blank=True)
    goodreads = models.CharField('Goodreads', max_length=128, blank=True)
    position = models.CharField('Посада', max_length=128, blank=True)

    is_staff = models.BooleanField(
        'Співробітни(ця)к',
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between.
        """

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""

        return self.first_name
