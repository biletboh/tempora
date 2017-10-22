from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

from users.models import UserProfile
from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField() 
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    image = ThumbnailerImageField(upload_to='photos/blog', blank=True) 
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'

