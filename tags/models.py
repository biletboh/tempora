from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural = 'tags'

