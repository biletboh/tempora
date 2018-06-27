from ajax_select import register, LookupChannel
from users.models import UserProfile


@register('curators')
class CuratorLookup(LookupChannel):

    model = UserProfile

    def get_query(self, q, request):
        queryset = self.model.objects.filter(last_name__icontains=q)
        return queryset.order_by('email')[:20]

    def format_item_display(self, item):
        tag = u'<span class="custom-tag">%s %s</span>' % (item.first_name,
                                                          item.last_name)
        return tag
