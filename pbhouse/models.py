from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField


class UserProfile(models.Model):
    user = models.OneToOneField(
                            settings.AUTH_USER_MODEL, unique=True,
                            primary_key=True, on_delete=models.CASCADE,
                            related_name='user_profile')
    avatar = ThumbnailerImageField(upload_to='profile_images', blank=True)
    info = models.CharField(max_length=512)
    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    linkedin = models.CharField(max_length=128)
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

