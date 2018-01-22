from ajax_select import register, LookupChannel
from users.models import UserProfile


@register('curators')
class CuratorLookup(LookupChannel):

    model = UserProfile

    def get_query(self, q, request):
        queryset = self.model.objects.filter(email__icontains=q)
        return queryset.order_by('email')[:20]

    def format_item_display(self, item):
        tag = u'<span class="custom-tag">%s</span>' % item.email
        return tag
