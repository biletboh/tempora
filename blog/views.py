from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView,\
        DeleteView, ListView, UpdateView, CreateView

from django_filters.views import FilterView

from blog.models import Post
from blog.forms import PostModelForm
from blog.filters import PostFilter


class PostList(ListView):
    """Render List of posts."""

    model = Post
    context_object_name = "posts"
    template_name = 'blog/blog.html'
    paginate_by = 10
    queryset = Post.objects.all().exclude(selected=True)


class Page(DetailView):
    """Render Post Page."""

    model = Post
    template_name = 'blog/page.html'


class CreatePost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create Posts."""

    form_class = PostModelForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:update_list')
    success_message = 'Запис додано!'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdatePost(LoginRequiredMixin, UpdateView):
    """Update a post."""

    model = Post
    form_class = PostModelForm
    template_name = 'blog/update.html'
    success_message = 'Запис оновлено!'

    def get_success_url(self):
        return reverse_lazy('blog:update', kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.object.user
        return kwargs


class DeletePost(LoginRequiredMixin, DeleteView):
    """Delete a Post."""

    model = Post
    success_url = reverse_lazy('blog:update_list')


class UpdatePostList(LoginRequiredMixin, FilterView):
    """Render a list of Posts to edit."""

    model = Post
    template_name = 'blog/update_list.html'
    context_object_name = 'posts'
    paginate_by = 20
    filterset_class = PostFilter
    queryset = Post.objects.all()
