# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-11 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20180111_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=140, verbose_name='Назва'),
        ),
    ]