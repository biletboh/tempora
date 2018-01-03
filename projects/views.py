from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from projects.forms import ProjectModelForm
from projects.models import Project
from core.mixins import IsSuperUserTestMixin


class ProjectPage(TemplateView):
    """Render projects page."""

    template_name = 'projects/project_page.html'


class ProjectCreate(IsSuperUserTestMixin, SuccessMessageMixin, CreateView):
    """Create projects."""

    model = Project
    form_class = ProjectModelForm
    fields = ('title', 'short_descr', 'description',
              'image', 'slug', 'curators')
    template_name = 'projects/create.html'
    success_url = reverse_lazy('users:create')
    login_url = reverse_lazy('users:profile')

