# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-16 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191014_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Посилання на сайті'),
        ),
    ]
