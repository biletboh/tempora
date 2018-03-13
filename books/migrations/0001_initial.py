# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-13 21:50
from __future__ import unicode_literals

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0002_auto_20180111_1854'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('short_descr', models.TextField(blank=True, verbose_name='Короткий опис')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('from_author', models.TextField(blank=True, verbose_name='Від автора')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публікації')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='photos/books', verbose_name='Світлина')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Ціна')),
                ('in_stock', models.CharField(blank=True, choices=[('0', 'Немає у наявності'), ('1', 'У наявності'), ('2', 'Очікується')], default='Тверда', max_length=1, verbose_name='У наявності')),
                ('release', models.DateField(blank=True, null=True, verbose_name='Дата виходу')),
                ('selected', models.BooleanField(default=False, verbose_name='Обрана книга')),
                ('new', models.BooleanField(default=False, verbose_name='Новинка')),
                ('best_seller', models.BooleanField(default=False, verbose_name='Топ продажів')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Сторінки')),
                ('cover', models.CharField(blank=True, choices=[('Hrd', 'Тверда'), ('Sft', "M'яка")], default='Тверда', max_length=3, verbose_name='Обкладинка')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Вага (г)')),
                ('height', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Висота')),
                ('length', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Ширина')),
                ('depth', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Глибина')),
                ('publisher', models.CharField(max_length=90, verbose_name='Видавництво')),
                ('isbn_13', models.CharField(blank=True, max_length=15, verbose_name='ISBN-13')),
                ('isbn_10', models.CharField(blank=True, max_length=15, verbose_name='ISBN-10')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Посилання')),
                ('authors', models.ManyToManyField(blank=True, to='authors.Author')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'verbose_name_plural': 'books',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публікації')),
                ('quantity', models.IntegerField(blank=True, default=1, verbose_name='Кількість')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=90, verbose_name='Емейл')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, verbose_name='Повідомлення')),
                ('comment', models.TextField(blank=True, verbose_name='Коментар')),
                ('processed', models.BooleanField(default=False, verbose_name='Опрацьовано')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='books.Book')),
            ],
            options={
                'verbose_name_plural': 'orders',
                'ordering': ('-date',),
            },
        ),
    ]
