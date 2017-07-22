from django.shortcuts import render
from django.views.generic import View, DetailView, FormView, TemplateView,\
        DeleteView, ListView 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
                image=form.cleaned_data['image'])
        post.save()
        form.delete_temporary_files()
        return super(CreatePost, self).form_valid(form)

