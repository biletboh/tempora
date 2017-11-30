from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, TemplateView, CreateView, DetailView,\
        FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from el_pagination.views import AjaxListView

from users.forms import UserCreateForm, UserUpdateForm,\
    ProfileUpdateForm
from users.models import UserProfile


class Profile(LoginRequiredMixin, TemplateView):
    """Render Profile page."""

    template_name='users/profile.html'

    def get_login_url(self):
        return reverse_lazy('account_login')


class CreateUser(
                LoginRequiredMixin, UserPassesTestMixin,
                SuccessMessageMixin, FormView):
    """
    Create User.
    """

    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:create')
    login_url = reverse_lazy('users:profile')
    success_message = _('A user was created successfully')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        position = form.cleaned_data['position']
        info = form.cleaned_data['info']
        is_staff = form.cleaned_data['is_staff']
        is_active = form.cleaned_data['is_active']
        facebook = form.cleaned_data['facebook']
        twitter = form.cleaned_data['twitter']
        linkedin = form.cleaned_data['linkedin']
        goodreads = form.cleaned_data['goodreads']
        avatar = form.cleaned_data['avatar']
        password = form.cleaned_data['password1']
        team = form.cleaned_data['team']
        authors = form.cleaned_data['authors']
        bloggers = form.cleaned_data['bloggers']

        user = UserProfile.objects.create(
                                        email=email, first_name=first_name,
                                        last_name=last_name, position=position,
                                        is_staff=is_staff,
                                        is_active=is_active, facebook=facebook,
                                        twitter=twitter, linkedin=linkedin,
                                        goodreads=goodreads, avatar=avatar
                                        )
        user.set_password(password)
        user.groups.add(team)
        user.groups.add(authors)
        user.groups.add(bloggers)

        user.save()

        return super(CreateUser, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateUser, self).get_context_data(**kwargs)
        context['title'] = _('Create User')
        return context

    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = _('You have to be a superuser to access this page.')
            messages.warning(self.request, denied)
        return user


class DisplayUser(DetailView):
    """Get UserProfile for editting."""

    model = UserProfile
    template_name = 'users/edit.html'
    login_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super(DisplayUser, self).get_context_data(**kwargs)
        team = self.object.groups.filter(name='Team').exists()
        authors = self.object.groups.filter(name='Authors').exists()
        bloggers = self.object.groups.filter(name='Bloggers').exists()

        initial = {
                'email': self.object.email,
                'first_name': self.object.first_name,
                'last_name': self.object.last_name,
                'position': self.object.position,
                'info': self.object.info,
                'facebook': self.object.facebook,
                'twitter': self.object.twitter,
                'linkedin': self.object.linkedin,
                'is_active': self.object.is_active,
                'is_staff': self.object.is_staff,
                'team': team,
                'authors': authors,
                'bloggers': bloggers,
                }

        context['form'] = self.get_update_form(initial=initial)
        context['title'] = _('Edit Users')
        return context

    def get_update_form(self, initial):
        super_user = self.request.user.is_superuser
        if super_user:
            return UserUpdateForm(initial=initial)
        else:
            del initial['is_active']
            del initial['is_staff']
            del initial['team']
            del initial['authors']
            del initial['bloggers']
            del initial['position']
            return ProfileUpdateForm(initial=initial)


class UpdateUser(SuccessMessageMixin, SingleObjectMixin, FormView):
    """Update a User."""

    form_class = UserUpdateForm
    model = UserProfile
    success_message = _("A user was updated successfully")
    template_name = 'users/edit.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateUser, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        params = {'pk': self.object.pk}
        user = UserProfile.objects.get(**params)
        user.email = form.cleaned_data['email']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.position = form.cleaned_data['position']
        user.is_staff = form.cleaned_data['is_staff']
        user.is_active = form.cleaned_data['is_active']
        user.info = form.cleaned_data['info']
        user.facebook = form.cleaned_data['facebook']
        user.twitter = form.cleaned_data['twitter']
        user.likedin = form.cleaned_data['linkedin']
        user.goodreads = form.cleaned_data['goodreads']

        # Check if the user has prviviledges to edit 
        # group membership and user active status.
        current_user = self.request.user
        if current_user.is_superuser:
            user.is_staff = form.cleaned_data['is_staff']
            user.is_active = form.cleaned_data['is_active']
            self.set_user_group(form, user, 'Team')
            self.set_user_group(form, user, 'Authors')
            self.set_user_group(form, user, 'Bloggers')

        # set avatar
        avatar = form.cleaned_data['avatar']
        if avatar:
            user.avatar = avatar

        # set user password
        password = form.cleaned_data['password1']
        if password:
            user.set_password(password)

        # save user updates
        user.save()

        # delete temporary files
        form.delete_temporary_files()

        return super(UpdateUser, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:edit', kwargs={'pk': self.object.pk})

    def set_user_group(self, form, user, name):
        try:
            group = Group.objects.get(name=name)
        except:
            raise Exception('Group does not exist.')

        # add or remove group membership 
        checked = form.cleaned_data[name.lower()]
        print('form', checked)
        if checked:
            user.groups.add(group)
        else:
            user.groups.remove(group)
        return user


class EditUser(LoginRequiredMixin, UserPassesTestMixin, View):
    """Edit Users."""

    login_url = reverse_lazy('users:dashboard')

    def get(self, request, *args, **kwargs):
        view = DisplayUser.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdateUser.as_view()
        return view(request, *args, **kwargs)

    def test_func(self):
        super_user = self.request.user.is_superuser
        profile_user = self.request.user.pk
        access_user = int(self.kwargs['pk'])
        denied = _('You have to be a superuser to access this page.')

        if super_user or (profile_user==access_user):
            return True

        messages.warning(self.request, denied)
        return False


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a User."""

    model = UserProfile
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:user_list')
    login_url = reverse_lazy('users:dashboard')

    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = _('You have to be a superuser to access this page.')
            messages.warning(self.request, denied)
        return user


class EditUserList(LoginRequiredMixin, UserPassesTestMixin, AjaxListView):
    """
    Render a list of Users to edit with ajax endless pagination.
    """

    context_object_name = "users"
    template_name = 'users/user_list.html'
    page_template = 'users/users.html'
    login_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(EditUserList, self).get_context_data(**kwargs)
        context['title'] = 'User Edit list'
        return context

    def get_queryset(self):
        return UserProfile.objects.all()

    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = _('You have to be a superuser to access this page.')
            messages.warning(self.request, denied)
        return user

