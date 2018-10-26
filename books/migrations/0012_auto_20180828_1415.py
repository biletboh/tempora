# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-28 11:15
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Ціна'),
        ),
    ]