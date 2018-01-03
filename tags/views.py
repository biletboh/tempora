from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, DetailView, FormView, TemplateView,\
        DeleteView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from el_pagination.views import AjaxListView

from tags.models import Tag
from tags.forms import TagForm


class CreateTag(SuccessMessageMixin, FormView):
    """
    Create a tag.
    """

    form_class = TagForm 
    template_name = 'tags/create.html'
    success_url = reverse_lazy('tags:edit_list')
    login_url = reverse_lazy('pbhouse:dashboard') 
    success_message = _('Тег додано.') 

    def form_valid(self, form):
        tag = Tag(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                )
        tag.save()
        form.delete_temporary_files()
        return super(CreateTag, self).form_valid(form)

    def test_func(self):
        user = self.request.user.is_staff
        if not user:
            denied = _('У вас немає повноважень, щоб переглядати цю сторінку.')
            messages.warning(self.request, denied)
        return user

