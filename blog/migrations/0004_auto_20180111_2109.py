# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-11 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_merge_20171130_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_descr',
            field=tinymce.models.HTMLField(blank=True, max_length=256, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
    ]
