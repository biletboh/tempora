# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-27 15:18
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20181227_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='photos/projects', verbose_name='Іконка'),
        ),
    ]
