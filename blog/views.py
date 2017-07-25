from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View, DetailView, FormView, TemplateView,\
        DeleteView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from el_pagination.views import AjaxListView

from blog.models import Post
from blog.forms import PostForm


class PostList(AjaxListView):
    """
    Render List of posts.
    """

    context_object_name = "posts"
    template_name = 'blog/blog.html'
    page_template = 'blog/post_list.html'

    def get_queryset(self): 
        return Post.objects.all()


class Page(DetailView):
    """
    Render Post Page.
    """

    model = Post 
    template_name = 'blog/page.html'


class CreatePost(SuccessMessageMixin, FormView):
    """
    Create Posts.
    """

    form_class = PostForm 
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:blog')
    #login_url = reverse_lazy('blog:blog') 
    success_message = "A post was created successfully"

    def form_valid(self, form):
        post = Post(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                image=form.cleaned_data['image'],
                user=self.request.user)
        post.save()
        form.delete_temporary_files()
        return super(CreatePost, self).form_valid(form)


class DisplayPost(DetailView):
    """
    Get Post for editting.
    """

    model = Post 
    template_name = 'blog/edit.html'
    login_url = reverse_lazy('users:dashboard') 

    def get_context_data(self, **kwargs):
        context = super(DisplayPost, self).get_context_data(**kwargs)

        initial = {
                'title': self.object.title,
                'body': self.object.body,
                }

        context['form'] = PostForm(initial=initial) 

        return context

class UpdatePost(SuccessMessageMixin, SingleObjectMixin, FormView):
    """
    Update a Post.
    """

    form_class = PostForm 
    model = Post 
    success_message = _("A post was updated successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdatePost, self).post(request, *args, **kwargs)
 
    def form_valid(self, form):
        params = {'pk': self.object.pk}
        post = Post.objects.get(**params)

        post.title= form.cleaned_data['title'] 
        post.body = form.cleaned_data['body'] 
        image = form.cleaned_data['image']

        if image: 
            post.image = image
        post.save()

        form.delete_temporary_files()

        return super(UpdatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:edit', kwargs={'pk': self.object.pk})


class EditPost(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Edit Post.
    """
    
    login_url = reverse_lazy('users:dashboard')

    def get(self, request, *args, **kwargs):
        view = DisplayPost.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdatePost.as_view()
        return view(request, *args, **kwargs)

    def test_func(self):
        super_user = self.request.user.is_superuser

        if super_user:
            return True 

        denied = _('У вас бракує дозволу, щоб переглядати цю сторінку.')
        messages.warning(self.request, denied)
        return False 


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a User.
    """

    model = UserProfile 
    success_url = reverse_lazy('users:user_list')
    login_url = reverse_lazy('users:dashboard')
    
    def test_func(self):
        super_user = self.request.user.is_superuser

        if super_user:
            return True 

        denied = _('У вас бракує дозволу, щоб переглядати цю сторінку.')
        messages.warning(self.request, denied)
        return False 

