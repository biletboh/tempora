from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView,\
        DeleteView, ListView, UpdateView, CreateView

from video.models import Video
from video.forms import VideoModelForm


class VideoList(ListView):
    """Render List of videos."""

    model = Video
    context_object_name = 'objects'
    template_name = 'video/list.html'
    paginate_by = 10
    queryset = Video.objects.all()


class Page(DetailView):
    """Render Video Page."""

    model = Video
    template_name = 'video/page.html'


class CreateVideo(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create videos."""

    form_class = VideoModelForm
    template_name = 'video/create.html'
    success_url = reverse_lazy('video:update_list')
    success_message = 'Запис додано!'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateVideo(LoginRequiredMixin, UpdateView):
    """Update a video."""

    model = Video
    form_class = VideoModelForm
    template_name = 'video/update.html'
    success_message = 'Запис оновлено!'

    def get_success_url(self):
        return reverse_lazy('video:update', kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.object.user
        return kwargs


class DeleteVideo(LoginRequiredMixin, DeleteView):
    """Delete a video."""

    model = Video
    success_url = reverse_lazy('video:update_list')


class UpdateVideoList(LoginRequiredMixin, ListView):
    """Render a list of videos to edit."""

    model = Video
    template_name = 'video/update_list.html'
    context_object_name = 'objects'
    paginate_by = 20
    queryset = Video.objects.all()
