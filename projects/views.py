from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from projects.models import Project


class ProjectPage(TemplateView):
    """Render projects page."""

    template_name = 'projects/project_page.html'


class ProjectCreate(CreateView):
    """Create projects."""

    model = Project
    fields = ('title', 'short_descr', 'description',
              'image', 'slug', 'curators')
    template_name = 'projects/create.html'

