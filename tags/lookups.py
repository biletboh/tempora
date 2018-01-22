from ajax_select import register, LookupChannel
from tags.models import Tag


@register('tags')
class TagsLookup(LookupChannel):

    model = Tag

    def get_query(self, q, request):
        queryset = self.model.objects.filter(title__icontains=q)
        return queryset.order_by('title')[:20]

    def format_item_display(self, item):
        tag = u'<span class="custom-tag">%s</span>' % item.title
        return tag
