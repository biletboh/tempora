from urllib.parse import urlencode
from django import template


register = template.Library()


@register.simple_tag(takes_context=True, name='filter_page')
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
