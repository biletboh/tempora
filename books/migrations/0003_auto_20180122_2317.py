# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 21:17
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180111_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='depth',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Глибина'),
        ),
        migrations.AlterField(
            model_name='book',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Висота'),
        ),
        migrations.AlterField(
            model_name='book',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.1'))], verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, verbose_name='Сторінки'),
        ),
    ]
