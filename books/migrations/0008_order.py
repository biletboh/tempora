# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-24 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180129_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, verbose_name='Кількість')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=90, verbose_name='Емейл')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, verbose_name='Опис')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='books.Book')),
            ],
        ),
    ]
