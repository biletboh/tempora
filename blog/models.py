from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

from core.models import AbstractPublication
from tags.models import Tag


class Post(AbstractPublication):
    """Store post data for a blog."""

    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    body = HTMLField('Текст', blank=True)
    image = ThumbnailerImageField('Світлина', upload_to='photos/blog',
                                  blank=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'
