# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-27 10:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20180411_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn_10',
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=60, verbose_name='ISBN-13'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Рік у форматі: <YYYY>', null=True, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2023)], verbose_name='Рік Видання'),
        ),
    ]
