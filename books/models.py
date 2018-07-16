from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

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
                                    default=timezone.now)
    pub_year = models.CharField('Рік видання', max_length=50, blank=True,
                                default='')
    release = models.DateField('Дата виходу', null=True, blank=True)
    image = ThumbnailerImageField('Світлина', upload_to='photos/books',
                                  blank=True)
    price = models.DecimalField(
                        'Ціна', max_digits=8, decimal_places=2,
                        validators=[MinValueValidator(Decimal('0.01'))],
                        blank=True, null=True)
    in_stock = models.CharField('У наявності', max_length=1,
                                default=IN_STOCK[0][0], choices=IN_STOCK,
                                blank=True)
    selected = models.BooleanField('Обрана книга', default=False, blank=True)
    new = models.BooleanField('Новинка', default=False, blank=True)
    best_seller = models.BooleanField('Топ продажів', default=False,
                                      blank=True)
    pages = models.CharField('Сторінки', max_length=50, blank=True, default='')
    cover = models.CharField('Обкладинка', max_length=3, default=COVERS[0][0],
                             choices=COVERS, blank=True)
    weight = models.PositiveSmallIntegerField('Вага (г)', null=True,
                                              blank=True)
    height = models.PositiveSmallIntegerField('Висота', blank=True, null=True)
    length = models.PositiveSmallIntegerField('Ширина', blank=True, null=True)
    publisher = models.CharField('Видавництво', max_length=90, blank=True)
    isbn_13 = models.CharField('ISBN-13', max_length=256, blank=True)

    authors = models.ManyToManyField(Author, blank=True)
    translators = models.CharField('Переклад', max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)
    slug = models.SlugField('Посилання', unique=True, null=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title

    def show_size(self):
        size = f'{self.height}x{self.length}'
        if (not self.height) or (not self.length):
            size = ''
        return size

    def isbn_list(self):
        return self.isbn_13.split(' ')


class Order(models.Model):
    """Book order."""

    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='orders')
    date = models.DateTimeField('Час замовлення',
                                default=timezone.now)
    quantity = models.PositiveSmallIntegerField('Кількість', default=1,
                                                blank=True)
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
