from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,\
        ListView, UpdateView, DeleteView

from tags.models import Tag


class CreateTag(SuccessMessageMixin, CreateView):
    """Create a tag."""

    model = Tag
    fields = ('title', 'description')
    template_name = 'tags/create.html'
    success_url = reverse_lazy('tags:admin_list')
    success_message = 'Тег додано!'


class UpdateTag(SuccessMessageMixin, UpdateView):
    """Update a tag."""

    model = Tag
    fields = ('title', 'description')
    template_name = 'tags/update.html'
    success_url = reverse_lazy('tags:update')
    success_message = 'Тег оновлено!'


class DeleteTag(SuccessMessageMixin, DeleteView):
    """Delete a tag."""

    model = Tag
    success_url = reverse_lazy('tags:admin_list')
    login_url = reverse_lazy('users:dashboard')
    success_message = 'Тег видалено!'


class AdminTagList(ListView):
    """Render a list of tags to edit."""

    model = Tag
    context_object_name = 'tags'
    template_name = 'tags/list.html'
    paginate_by = 10
    queryset = Tag.objects.all()
