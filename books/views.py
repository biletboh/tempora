from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView,\
        ListView, UpdateView, DeleteView

from rest_framework.generics import CreateAPIView

from books.forms import BookModelForm, OrderModelForm
from books.models import Book, Order
from books.serializers import OrderSerializer


class BookList(ListView):
    """Render list of books."""

    model = Book
    context_object_name = 'books'
    template_name = 'books/list.html'
    paginate_by = 12
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['order_form'] = OrderModelForm
        return context


class BookPage(DetailView):
    """Render a book page."""

    model = Book
    template_name = 'books/page.html'

    def get_context_data(self, **kwargs):
        context = super(BookPage, self).get_context_data(**kwargs)
        context['order_form'] = OrderModelForm
        return context


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


class OrderList(ListView):
    """Render list of book orders."""

    model = Order
    context_object_name = 'orders'
    template_name = 'books/order_list.html'
    paginate_by = 20
    queryset = Order.objects.all()


class CreateOrder(CreateAPIView):
    """Create a book order."""

    authentication_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
