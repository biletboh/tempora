from django.db.models import Q

import django_filters

from .models import Author


class AuthorFilter(django_filters.FilterSet):
    """Filter authors."""

    authors = django_filters.CharFilter(method="filter_authors")

    class Meta:
        model = Author
        fields = {"authors": ["exact"]}

    def filter_authors(self, queryset, field_name, value):
        filter_args = Q()
        query = value.split()
        for part in query:
            if "." in part:
                part = part.replace(".", "")
                filter_args = filter_args & Q(first_name__icontains=part)
            else:
                filter_args = filter_args & Q(last_name__icontains=part) | Q(
                    first_name__icontains=part
                )
                filter_args = (
                    filter_args
                    | Q(last_name__icontains=part)
                    | Q(first_name__icontains=part)
                )
        return queryset.filter(filter_args).distinct()
