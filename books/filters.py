from django import forms
from django.db import models

import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    """Filter books."""

    class Meta:
        model = Book
        fields = ['in_stock', 'selected', 'new', 'best_seller', 'tags']
        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
         }
