from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,\
        ListView, UpdateView, DeleteView

from books.forms import BookModelForm
from books.models import Book


class BookList(ListView):
    """Render list of books."""

    model = Book
    context_object_name = 'books'
    template_name = 'books/list.html'
    paginate_by = 10
    queryset = Book.objects.all()


class BookPage(DetailView):
    """Render a book page."""

    model = Book
    template_name = 'books/page.html'


class CreateBook(SuccessMessageMixin, CreateView):
    """Create a book."""

    form_class = BookModelForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books:update_list')
    success_message = 'Книгу додано!'


class UpdateBook(SuccessMessageMixin, UpdateView):
    """Update a book."""

    model = Book
    form_class = BookModelForm
    template_name = 'books/update.html'
    success_message = 'Книгу оновлено!'

    def get_success_url(self):
        return reverse_lazy('books:update', kwargs={'slug': self.object.slug})


class DeleteBook(SuccessMessageMixin, DeleteView):
    """Delete a book."""

    model = Book
    success_url = reverse_lazy('books:update_list')
    login_url = reverse_lazy('users:dashboard')
    success_message = 'Книгу видалено!'


class UpdateBookList(ListView):
    """Render a list of books to edit."""

    model = Book
    context_object_name = 'books'
    template_name = 'books/update_list.html'
    paginate_by = 10
    queryset = Book.objects.all()
