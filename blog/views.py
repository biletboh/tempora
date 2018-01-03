from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
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
    queryset = Post.objects.all()


class Page(DetailView):
    """Render Post Page."""

    model = Post
    template_name = 'blog/page.html'


class CreatePost(SuccessMessageMixin, CreateView):
    """Create Posts."""

    form_class = PostModelForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:edit_list')
    success_message = "A post was created successfully"

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdatePost(UpdateView):
    """Update an internal deposit."""

    model = Post
    form_class = PostModelForm
    template_name = 'blog/update.html'
    success_message = 'Пост оновлено.'

    def get_success_url(self):
        return reverse_lazy('blog:update', kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        kwargs = super(UpdatePost, self).get_form_kwargs()
        kwargs['user'] = self.object.user
        return kwargs


class DeletePost(DeleteView):
    """Delete Post."""

    model = Post
    success_url = reverse_lazy('blog:edit_list')
    login_url = reverse_lazy('users:dashboard')


class EditPostList(LoginRequiredMixin, FilterView):
    """Render a list of Posts to edit with ajax endless pagination."""

    model = Post
    template_name = 'blog/edit_list.html'
    context_object_name = 'posts'
    paginate_by = 20
    login_url = reverse_lazy('users:dashboard')
    filterset_class = PostFilter

    def get_queryset(self):
        return Post.objects.all()
