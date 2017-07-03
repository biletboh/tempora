from django.shortcuts import render
from django.views.generic import View, DetailView, CreateView, DeleteView,\
        TemplateView
from users.models import UserProfile as UserProfileModel


class LandingPage(TemplateView):
    template_name='pbhouse/landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['title'] = "Tempora Landing"
        return context


class UserProfile(TemplateView):
    template_name='users/profile.html'


class Team(TemplateView):
    """
    Render Team page.
    """

    template_name='pbhouse/team.html'

    def get_context_data(self, **kwargs):
        context = super(Team, self).get_context_data(**kwargs)
        context['team'] = UserProfileModel.objects.all()
        return context

