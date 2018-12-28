from django.db import models
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField
from transliterate import slugify

from tags.models import Tag
from users.models import UserProfile


class Project(models.Model):
    """Store projects data."""

    title = models.CharField('Назва', max_length=200)
    short_descr = models.CharField('Короткий опис', max_length=256)
    description = models.CharField('Опис', max_length=2000)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.now)
    image = ThumbnailerImageField(
        'Світлина', upload_to='photos/projects')
    icon_image = ThumbnailerImageField(
        'Іконка', upload_to='photos/projects', null=True)
    curators = models.ManyToManyField(UserProfile, related_name='projects')
    project_tag = models.ForeignKey(Tag, related_name='project_tag', null=True)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Project %s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
