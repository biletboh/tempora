from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django_filters.views import FilterView

from authors.forms import AuthorModelForm
from authors.models import Author
from authors.filters import AuthorFilter


class AuthorList(ListView):
    """Render list of authors."""

    model = Author
    context_object_name = "authors"
    template_name = "authors/list.html"
    paginate_by = 10
    queryset = Author.objects.all()


class AuthorPage(DetailView):
    """Render an author page."""

    model = Author
    template_name = "authors/page.html"


class CreateAuthor(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create an author."""

    form_class = AuthorModelForm
    template_name = "authors/create.html"
    success_url = reverse_lazy("authors:update_list")
    success_message = "Автора додано!"


class UpdateAuthor(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update an author."""

    model = Author
    form_class = AuthorModelForm
    template_name = "authors/update.html"
    success_message = "Автора оновлено!"

    def get_success_url(self):
        return reverse_lazy(
            "authors:update", kwargs={"slug": self.object.slug}
        )


class DeleteAuthor(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete an author."""

    model = Author
    success_url = reverse_lazy("authors:admin_list")
    success_message = "Автора видалено!"


class UpdateAuthorList(LoginRequiredMixin, FilterView):
    """Render a list of authors to edit."""

    model = Author
    context_object_name = "authors"
    template_name = "authors/update_list.html"
    paginate_by = 10
    queryset = Author.objects.all()
    filterset_class = AuthorFilter
