from django.db import models
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField
from transliterate import slugify

from tags.models import Tag


class Author(models.Model):
    """Store book information."""

    first_name = models.CharField("Ім'я", max_length=200)
    last_name = models.CharField('Прізвище', max_length=200)
    about_author = models.TextField('Про автора', blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.now)
    image = ThumbnailerImageField('Світлина', upload_to='photos/blog',
                                  blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True, blank=True)

    class Meta:
        ordering = ('last_name',)
        verbose_name_plural = 'authors'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + '-' + self.last_name)
        super().save(*args, **kwargs)
