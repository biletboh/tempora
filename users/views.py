from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView

from users.filters import UserFilter
from users.forms import AccountUserModelForm, UserModelForm
from users.models import UserProfile


class CreateUser(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create User."""

    form_class = UserModelForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:update_list')
    success_message = 'Акаунт створено.'


class UpdateUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update users."""

    model = UserProfile
    form_class = UserModelForm
    template_name = 'users/update.html'
    success_message = 'Акаунт оновлено.'

    def get_success_url(self):
        return reverse_lazy('users:update', kwargs={'pk': self.object.pk})


class AccountUpdateUser(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update a personal profile."""

    model = UserProfile
    form_class = AccountUserModelForm
    template_name = 'users/update.html'
    success_message = 'Акаунт оновлено.'

    def get_success_url(self):
        return reverse_lazy('users:update', kwargs={'pk': self.object.pk})


class DeleteUser(LoginRequiredMixin, DeleteView):
    """Delete a User."""

    model = UserProfile
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:update_list')


class UserList(LoginRequiredMixin, SuccessMessageMixin, FilterView):
    """Render a list of Users to edit."""

    model = UserProfile
    template_name = 'users/update_list.html'
    context_object_name = "users"
    paginate_by = 20
    filterset_class = UserFilter

    def get_queryset(self):
        return UserProfile.objects.all()
