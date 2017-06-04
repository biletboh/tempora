from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField() 
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    image = ThumbnailerImageField(upload_to='photos/blog', blank=True) 
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'

