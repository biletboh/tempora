from django.shortcuts import render
from django.views.generic import View, DetailView, CreateView, DeleteView,\
        TemplateView


class LandingPage(TemplateView):
    template_name='pbhouse/landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['title'] = "Tempora Landing"
        return context

