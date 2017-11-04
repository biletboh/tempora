from django.shortcuts import render
from django.views.generic import TemplateView 


class ProjectPage(TemplateView):
    """Render projects page."""

    template_name='projects/project_page.html'

