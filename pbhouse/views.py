from django.http import JsonResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView

from blog.models import Post
from books.models import Book
from pbhouse.forms import ContactForm
from pbhouse.utils import send_contact_message
from projects.models import Project
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
    """Render landing page and contact form."""

    template_name = 'pbhouse/landing.html'
    form_class = ContactForm
    success_url = reverse_lazy('pbhouse:landing')
    success_message = _('A user was created successfully')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        send_contact_message(name, email, phone, message)

        return super(LandingPage, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:3]
        context['projects'] = Project.objects.all()
        context['books'] = Book.objects.all()[:15]
        return context


class Team(TemplateView):
    """Render Team page."""

    template_name = 'pbhouse/team.html'

    def get_context_data(self, **kwargs):
        context = super(Team, self).get_context_data(**kwargs)
        context['team'] = UserProfileModel.objects.filter(groups__name='Team')
        return context
