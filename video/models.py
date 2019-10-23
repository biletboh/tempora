from django.db import models

from core.models import AbstractPublication
from tags.models import Tag


class Video(AbstractPublication):
    """Store data for a video."""

    tags = models.ManyToManyField(Tag, related_name='videos', blank=True)
    youtube = models.URLField('Youtube')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'videos'
