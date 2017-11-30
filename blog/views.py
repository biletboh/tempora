from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView,\
        DeleteView, ListView, UpdateView

from blog.models import Post
from blog.forms import PostModelForm


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


class CreatePost(SuccessMessageMixin, FormView):
    """Create Posts."""

    form_class = PostModelForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:edit_list')
    success_message = "A post was created successfully"

    def form_valid(self, form):
        form.delete_temporary_files()
        return super(CreatePost, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdatePost(UpdateView):
    """Update an internal deposit."""

    model = Post
    form_class = PostModelForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:update')
    success_message = 'Пост оновлено.'

    def get_form_kwargs(self):
        kwargs = super(UpdatePost, self).get_form_kwargs()
        kwargs['user'] = self.object.user
        return kwargs


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Post."""

    model = Post
    success_url = reverse_lazy('blog:edit_list')
    login_url = reverse_lazy('users:dashboard')


class EditPostList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Render a list of Posts to edit with ajax endless pagination."""

    context_object_name = "posts"
    template_name = 'blog/edit_list.html'
    page_template = 'blog/posts.html'
    login_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return Post.objects.all()
