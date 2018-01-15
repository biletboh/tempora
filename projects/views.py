from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView,\
    DeleteView, ListView

from projects.forms import ProjectModelForm
from projects.models import Project
from core.mixins import IsSuperUserTestMixin


class ProjectPage(TemplateView):
    """Render projects page."""

    template_name = 'projects/project_page.html'


class CreateProject(IsSuperUserTestMixin, SuccessMessageMixin, CreateView):
    """Create a project."""

    form_class = ProjectModelForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('projects:update_list')
    success_message = 'Проект додано!'


class UpdateProject(SuccessMessageMixin, UpdateView):
    """Update a project."""

    model = Project
    form_class = ProjectModelForm
    template_name = 'projects/update.html'
    success_message = 'Проект оновлено!'

    def get_success_url(self):
        return reverse_lazy('projects:update',
                            kwargs={'slug': self.object.slug})


class DeleteProject(SuccessMessageMixin, DeleteView):
    """Delete a project."""

    model = Project
    success_url = reverse_lazy('projects:update_list')
    login_url = reverse_lazy('users:dashboard')
    success_message = 'Проект видалено!'


class UpdateProjectList(ListView):
    """Render a list of projects to edit."""

    model = Project
    context_object_name = 'projects'
    template_name = 'projects/update_list.html'
    paginate_by = 10
    queryset = Project.objects.all()
