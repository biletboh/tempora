from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView,\
    DeleteView, ListView

from projects.forms import ProjectModelForm
from projects.models import Project


class ProjectList(ListView):
    """Render list of projects."""

    model = Project
    context_object_name = 'projects'
    template_name = 'projects/list.html'
    paginate_by = 15


class ProjectPage(DetailView):
    """Render projects page."""

    model = Project
    template_name = 'projects/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.project_tag.posts.all()[:3]
        context['books'] = self.object.project_tag.books.all()[:6]
        return context


class CreateProject(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create a project."""

    form_class = ProjectModelForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('projects:update_list')
    success_message = 'Проект додано!'


class UpdateProject(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update a project."""

    model = Project
    form_class = ProjectModelForm
    template_name = 'projects/update.html'
    success_message = 'Проект оновлено!'

    def get_success_url(self):
        return reverse_lazy('projects:update',
                            kwargs={'slug': self.object.slug})


class DeleteProject(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete a project."""

    model = Project
    success_url = reverse_lazy('projects:update_list')
    success_message = 'Проект видалено!'


class UpdateProjectList(LoginRequiredMixin, ListView):
    """Render a list of projects to edit."""

    model = Project
    context_object_name = 'projects'
    template_name = 'projects/update_list.html'
    paginate_by = 10
    queryset = Project.objects.all()
