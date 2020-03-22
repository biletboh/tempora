from datetime import timedelta

from django import template
from django.utils import timezone
from django.utils.timesince import timesince
from django.template.defaultfilters import date


register = template.Library()


@register.filter(name='prettydates', expects_localtime=True)
def prettydates(value):
    if value:

        delta = timedelta(days=1)
        if (timezone.now() - value) < delta:
            return timesince(value)

        delta = timedelta(days=365)
        if (timezone.now() - value) < delta:
            return date(value, 'j E H:i')

    return value
