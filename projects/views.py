from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView,\
    DeleteView, ListView

from blog.models import Post
from projects.forms import ProjectModelForm
from projects.models import Project
from core.mixins import IsSuperUserTestMixin


class ProjectPage(DetailView):
    """Render projects page."""

    model = Project
    template_name = 'projects/page.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectPage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:3]
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
