from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

from users.models import UserProfile
from tags.models import Tag


class Post(models.Model):
    """Store post data for a blog."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    title = models.CharField('Заголовок', max_length=128)
    short_descr = HTMLField('Короткий опис', max_length=256, blank=True)
    body = HTMLField('Текст', blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.datetime.now)
    image = ThumbnailerImageField('Світлина', upload_to='photos/blog',
                                  blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True)

    def __str__(self):
        return 'Post: %s' % self.title

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'
