# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2022-02-09 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20181227_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Прізвище'),
        ),
    ]
