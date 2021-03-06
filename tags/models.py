from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField('Назва', max_length=140)
    description = models.CharField('Опис', max_length=200, blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.now)

    class Meta:
        ordering = ('-title',)
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.title
