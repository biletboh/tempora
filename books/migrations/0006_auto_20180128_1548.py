# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-28 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20180127_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=90, verbose_name='Видавництво'),
        ),
    ]
