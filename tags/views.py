from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,\
        ListView, UpdateView, DeleteView

from tags.forms import TagModelForm
from tags.models import Tag


class CreateTag(SuccessMessageMixin, CreateView):
    """Create a tag."""

    model = Tag
    form_class = TagModelForm
    template_name = 'tags/create.html'
    success_url = reverse_lazy('tags:update_list')
    success_message = 'Тег додано!'


class UpdateTag(SuccessMessageMixin, UpdateView):
    """Update a tag."""

    model = Tag
    form_class = TagModelForm
    template_name = 'tags/update.html'
    success_url = reverse_lazy('tags:update')
    success_message = 'Тег оновлено!'

    def get_success_url(self):
        return reverse_lazy('tags:update', kwargs={'pk': self.object.pk})


class DeleteTag(SuccessMessageMixin, DeleteView):
    """Delete a tag."""

    model = Tag
    success_url = reverse_lazy('tags:update_list')
    login_url = reverse_lazy('users:dashboard')
    success_message = 'Тег видалено!'


class AdminTagList(ListView):
    """Render a list of tags to edit."""

    model = Tag
    context_object_name = 'tags'
    template_name = 'tags/update_list.html'
    paginate_by = 10
    queryset = Tag.objects.all()
