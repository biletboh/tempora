from django.db.models import Q

import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    """Filter books."""

    authors = django_filters.CharFilter(method='filter_authors')

    class Meta:
        model = Book
        fields = {'title': ['icontains'],
                  'in_stock': ['exact'],
                  'selected': ['exact'],
                  'new': ['exact'],
                  'best_seller': ['exact'],
                  'tags': ['exact'],
                  'authors': ['exact']
                  }

    def filter_authors(self, queryset, field_name, value):
        filter_args = Q()
        query = value.split()
        for part in query:
            if '.' in part:
                part = part.replace('.', '')
                filter_args = (
                    filter_args & Q(authors__first_name__icontains=part))
            else:
                filter_args = (
                    filter_args & Q(authors__last_name__icontains=part)
                    | Q(authors__first_name__icontains=part))
                filter_args = (
                    filter_args | Q(authors__last_name__icontains=part)
                    | Q(authors__first_name__icontains=part))
        return queryset.filter(filter_args).distinct()
