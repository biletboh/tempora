# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-04 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180127_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='selected',
            field=models.BooleanField(default=False, verbose_name='Обраний пост'),
        ),
    ]