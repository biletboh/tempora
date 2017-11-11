from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView,\
        DeleteView, DetailView, ListView

from projects.forms import ProjectModelForm
from projects.models import Project
from core.mixins import IsSuperUserTestMixin


class ProjectPage(DetailView):
    """Render a project detail page."""

    model = Project
    template_name = 'projects/project_page.html'


class ProjectCreate(IsSuperUserTestMixin, SuccessMessageMixin, CreateView):
    """Create projects."""

    model = Project
    form_class = ProjectModelForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('projects:create')
    login_url = reverse_lazy('users:profile')
    success_message = 'Проект створено.'


class ProjectUpdate(IsSuperUserTestMixin, SuccessMessageMixin, UpdateView):
    """Update projects."""

    model = Project
    form_class = ProjectModelForm
    template_name = 'projects/update.html'
    login_url = reverse_lazy('users:profile')
    success_message = 'Проект оновлено.'

    def get_success_url(self, **kwargs):
        slug = self.object.slug
        return reverse_lazy('projects:update', kwargs={'slug': slug})


class ProjectDelete(IsSuperUserTestMixin, SuccessMessageMixin, DeleteView):
    """Delete a Project."""

    model = Project
    success_url = reverse_lazy('projects:dashboard_projects')
    login_url = reverse_lazy('users:dashboard')
    success_message = 'Проект видалено.'


class BaseProjectList(ListView):
    """Provide base View to render List of Projects."""

    model = Project
    context_object_name = "projects"
    paginate_by = 10


class ProjectList(BaseProjectList):
    """Render List of Projects."""

    template_name = 'projects/project_list.html'


class DashboardProjectList(BaseProjectList):
    """Render List of Projects to edit in a dashboard."""

    template_name = 'projects/dashboard_projects.html'

