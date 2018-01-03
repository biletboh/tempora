# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 08:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='photos/blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name_plural': 'posts',
            },
        ),
    ]