from django.db import models
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField
from users.models import UserProfile


class Project(models.Model):
    """Store projects data."""

    title = models.CharField('Назва', max_length=200)
    short_descr = models.CharField('Короткий опис', max_length=256)
    description = models.CharField('Опис', max_length=2000)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.datetime.now)
    image = ThumbnailerImageField('Світлина',
                                  upload_to='photos/projects',
                                  blank=True)
    curators = models.ManyToManyField(UserProfile,
                                      related_name='projects')
    slug = models.SlugField('Посилання', unique=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Project %s' % self.title

