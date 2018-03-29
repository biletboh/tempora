from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

from easy_thumbnails.fields import ThumbnailerImageField
from phonenumber_field.modelfields import PhoneNumberField

from authors.models import Author
from tags.models import Tag


class Book(models.Model):
    """Store book information."""

    HARD = 'Hrd'
    SOFT = 'Sft'
    AWAITING = 'Очікується'
    AVAILABLE = 'У наявності'
    NOT_AVAILABLE = 'Немає у наявності'

    COVERS = ((HARD, 'Тверда'),
              (SOFT, "M'яка"))
    IN_STOCK = (('0', NOT_AVAILABLE),
                ('1', AVAILABLE),
                ('2', AWAITING),
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
    in_stock = models.CharField('У наявності', max_length=1,
                                default=IN_STOCK[0][0], choices=IN_STOCK,
                                blank=True)
    release = models.DateField('Дата виходу', null=True, blank=True)
    selected = models.BooleanField('Обрана книга', default=False, blank=True)
    new = models.BooleanField('Новинка', default=False, blank=True)
    best_seller = models.BooleanField('Топ продажів', default=False,
                                      blank=True)
    pages = models.IntegerField('Сторінки', null=True, blank=True)
    cover = models.CharField('Обкладинка', max_length=3, default=COVERS[0][0],
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
    publisher = models.CharField('Видавництво', max_length=90, blank=True)
    isbn_13 = models.CharField('ISBN-13', max_length=15, blank=True)
    isbn_10 = models.CharField('ISBN-10', max_length=15, blank=True)

    authors = models.ManyToManyField(Author, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField('Посилання', unique=True,
                            null=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title

    def show_size(self):
        size = '{self.height} x {self.length} x {self.depth}'
        if not self.depth:
            size = f'{self.height} x {self.length}'
        if (not self.height) or (not self.length):
            size = ''
        return size


class Order(models.Model):
    """Book order."""

    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='orders')
    date = models.DateTimeField('Дата публікації',
                                default=timezone.datetime.now)
    quantity = models.IntegerField('Кількість', default=1, blank=True)
    name = models.CharField("Ім'я", max_length=30, blank=True)
    email = models.EmailField('Емейл', max_length=90)
    phone = PhoneNumberField('Телефон')
    message = models.TextField('Повідомлення', blank=True)
    comment = models.TextField('Коментар', blank=True)
    processed = models.BooleanField('Опрацьовано', default=False)

    def __str__(self):
        return f'{self.book.title} by {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'orders'
