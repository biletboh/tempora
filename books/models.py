from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

from easy_thumbnails.fields import ThumbnailerImageField

from authors.models import Author
from tags.models import Tag


class Book(models.Model):
    """Store book information."""

    COVERS = (('Тверда', 'Тверда'),
              ("M'яка", "M'яка"))
    IN_STOCK = (('Так', 'Так'),
                ('Ні', 'Ні'),
                ('Очікується', 'Очікується'),
                )

    title = models.CharField('Заголовок', max_length=200)
    short_descr = models.TextField('Короткий опис', blank=True)
    description = models.TextField('Опис', blank=True)
    from_author = models.TextField('Від автора', blank=True)
    pub_date = models.DateTimeField('Дата публікації',
                                    default=timezone.datetime.now)
    image = ThumbnailerImageField('Світлина', upload_to='photos/books',
                                  blank=True)

    price = models.DecimalField(
                        'Ціна', max_digits=8, decimal_places=2,
                        validators=[MinValueValidator(Decimal('0.01'))],
                        blank=True, null=True)
    in_stock = models.CharField('У наявності', max_length=10, default='Тверда',
                                choices=IN_STOCK, blank=True)
    pages = models.IntegerField('Сторінки', blank=True)
    cover = models.CharField('Обгортка', max_length=10, default='Тверда',
                             choices=COVERS, blank=True)
    weight = models.IntegerField('Вага (г)', null=True, blank=True)
    height = models.DecimalField(
                        'Висота', max_digits=6, decimal_places=1,
                        validators=[MinValueValidator(Decimal('0.1'))],
                        blank=True, null=True)
    length = models.DecimalField(
                        'Ширина', max_digits=6, decimal_places=1,
                        validators=[MinValueValidator(Decimal('0.1'))],
                        blank=True, null=True)
    depth = models.DecimalField(
                        'Глибина', max_digits=6, decimal_places=1,
                        validators=[MinValueValidator(Decimal('0.1'))],
                        blank=True, null=True)
    publisher = models.CharField('Видавництво', max_length=90,
                                 default='Видавничий дім "Темпора"')
    isbn_13 = models.CharField('ISBN-13', max_length=15, blank=True)
    isbn_10 = models.CharField('ISBN-10', max_length=15, blank=True)

    authors = models.ManyToManyField(Author, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True)

    class Meta:
        ordering = ('-title',)
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title

    def show_size(self):
        size = '%s x %s x %s' % (self.height, self.lenght, self.depth)
        if self.depth == '':
            size = '%s x %s' % (self.height, self.lenght)
        return size
