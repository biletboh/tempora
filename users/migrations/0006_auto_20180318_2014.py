# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-18 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180314_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this site.', verbose_name='staff status'),
        ),
    ]
