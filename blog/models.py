from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

from users.models import UserProfile


class Post(models.Model):
    """Store post data for a blog."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200)
    short_descr = HTMLField('Короткий опис', blank=True)
    body = HTMLField('Текст', blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.datetime.now)
    image = ThumbnailerImageField('Світлина', upload_to='photos/blog',
                                  blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'
