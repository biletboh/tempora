from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField
from transliterate import slugify

from users.models import UserProfile


class AbstractPublication(models.Model):
    """Abstract class to store general data about publications."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=128)
    short_descr = HTMLField('Короткий опис', max_length=256)
    selected = models.BooleanField('Обраний', default=False, blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.now)
    slug = models.SlugField('Посилання', unique=True, null=True, blank=True)

    class Meta:
        ordering = ('-pub_date',)
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
