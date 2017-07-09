import json
from django.http import JsonResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, DetailView, CreateView, DeleteView,\
        TemplateView, FormView

from pbhouse.forms import ContactForm
from users.models import UserProfile as UserProfileModel


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
            }

            return JsonResponse(data)
        else:
            return response


class LandingPage(SuccessMessageMixin, AjaxableResponseMixin, FormView):
    """
    Render landing page and contact form.
    """

    template_name = 'pbhouse/landing.html'
    form_class = ContactForm
    success_url = reverse_lazy('pbhouse:landing')
    success_message = _('A user was created successfully')
    
    def form_valid(self, form):
        name = form.cleaned_data['name'] 
        email = form.cleaned_data['email'] 
        phone = form.cleaned_data['phone'] 
        message = form.cleaned_data['message'] 
        print(name, email, phone, message)

        return super(LandingPage, self).form_valid(form)


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

