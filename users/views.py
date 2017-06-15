from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, TemplateView, CreateView, DetailView,\
        FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from el_pagination.views import AjaxListView

from users.forms import UserCreateForm, BaseUserProfileForm 
from users.models import UserProfile


class Profile(LoginRequiredMixin, TemplateView):
    """
    Render Profile page.
    """

    template_name='users/profile.html'
    
    def get_login_url(self):
        return reverse_lazy('account_login')

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['title'] = "UserProfile"
        return context


class CreateUser(
                LoginRequiredMixin, UserPassesTestMixin, 
                SuccessMessageMixin, FormView):
    """
    Create User.
    """

    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:create')
    login_url = reverse_lazy('account_signin')
    success_message = _('A user was created successfully')

    def form_valid(self, form):
        email = form.cleaned_data['email'] 
        first_name = form.cleaned_data['first_name'] 
        last_name = form.cleaned_data['last_name'] 
        is_staff = form.cleaned_data['is_staff'] 
        is_active = form.cleaned_data['is_active'] 
        facebook = form.cleaned_data['facebook'] 
        twitter = form.cleaned_data['twitter'] 
        linkedin = form.cleaned_data['linkedin'] 
        avatar = form.cleaned_data['avatar'] 
        password = form.cleaned_data['password1'] 

        user = UserProfile.objects.create(
                                        email=email, first_name=first_name,
                                        last_name=last_name, is_staff=is_staff,
                                        is_active=is_active, facebook=facebook,
                                        twitter=twitter, liknedin=linkedin,
                                        avatar=avatar
                                        )
        user.set_password(password)
        user.save()

        return super(CreateUser, self).form_valid(form)

    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = _('You have to be a superuser to access this page.')
            messages.warning(self.request, denied)
        return user

    def get_context_data(self, **kwargs):
        context = super(CreateUser, self).get_context_data(**kwargs)
        context['title'] = _('Create User')
        return context


class DisplayUser(DetailView):
    """
    Get UserProfile for editting.
    """

    model = UserProfile 
    template_name = 'users/edit.html'
    login_url = reverse_lazy('users:dashboard') 

    def get_context_data(self, **kwargs):
        context = super(DisplayUser, self).get_context_data(**kwargs)
        initial = {
                'email': self.object.email,
                'first_name': self.object.first_name,
                'last_name': self.object.last_name,
                'info': self.object.info,
                'facebook': self.object.facebook,
                'twitter': self.object.twitter,
                'linkedin': self.object.linkedin,
                'is_active': self.object.is_active,
                'is_staff': self.object.is_staff,
                }
        context['form'] = BaseUserProfileForm(initial=initial)
        context['title'] = _('Edit Users') 
        return context


class UpdateUser(SuccessMessageMixin, SingleObjectMixin, FormView):
    """
    Update a User.
    """

    form_class = BaseUserProfileForm 
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
        user.is_staff = form.cleaned_data['is_staff'] 
        user.is_active = form.cleaned_data['is_active'] 
        user.info = form.cleaned_data['info'] 
        user.facebook = form.cleaned_data['facebook'] 
        user.twitter = form.cleaned_data['twitter'] 
        user.likedin = form.cleaned_data['linkedin'] 
        user.save()
        return super(UpdateUser, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:edit', kwargs={'pk': self.object.pk})


class EditUser(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Edit Users.
    """
    
    def test_func(self):
        user = self.request.user.is_superuser
        if not user:
            denied = _('You have to be a superuser to access this page.')
            messages.warning(self.request, denied)
        return user

    def get(self, request, *args, **kwargs):
        view = DisplayUser.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdateUser.as_view()
        return view(request, *args, **kwargs)


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a User.
    """

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
    login_url = reverse_lazy('users:dashboard')

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

