# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_goodreads'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]