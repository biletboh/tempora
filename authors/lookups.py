from ajax_select import register, LookupChannel
from authors.models import Author


@register('authors')
class AuthorLookup(LookupChannel):

    model = Author

    def get_query(self, q, request):
        queryset = self.model.objects.filter(last_name__icontains=q)
        return queryset.order_by('last_name')[:20]

    def format_item_display(self, item):
        tag = u'<span class="custom-tag">%s %s</span>' % (item.first_name,
                                                          item.last_name)
        return tag
