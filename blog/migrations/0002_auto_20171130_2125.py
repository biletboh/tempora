# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-30 19:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import easy_thumbnails.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_descr',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Посилання'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='photos/blog', verbose_name='Світлина'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
