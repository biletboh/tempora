from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string

from books.models import Order


def send_order_notification(order_id):
    """Send a notification about the incoming order."""

    order = Order.objects.get(id=order_id)

    date = order.date.strftime('%Y-%m-%d %H:%M:%S')

    message = get_template('books/messages/notify.txt')
    context = {
        'name': order.name, 'email': order.email, 'phone': order.phone,
        'message': order.message, 'quantity': order.quantity,
        'book': order.book, 'id': order.id, 'date': date,
        'authors': order.book.show_authors,
        'address': order.address
        }
    body = message.render(context)

    html_message = render_to_string('books/messages/notify.html',
                                    context)
    title = (f'Нове замовлення №{order.id} від {order.name}: '
             + f'{order.book}')
    msg = EmailMultiAlternatives(
            title,
            body,
            settings.EMAIL_HOST_USER,
            [settings.NOTIFICATION_EMAIL],
            )
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def send_received_notification(order_id):
    """Send a notification about the receiving of the order
    to a customer."""

    order = Order.objects.get(id=order_id)

    date = order.date.strftime('%Y-%m-%d %H:%M:%S')

    title = 'Спасибі за ваше замовлення!'
    message = get_template('books/messages/notify_received.txt')
    context = {
        'book': order.book, 'id': order.id,
        'quantity': order.quantity,
        'authors': order.book.show_authors,
        'date': date, 'title': title
        }
    body = message.render(context)

    html_message = render_to_string('books/messages/notify_received.html',
                                    context)
    msg = EmailMultiAlternatives(
            title,
            body,
            settings.EMAIL_HOST_USER,
            [order.email],
            )
    msg.attach_alternative(html_message, "text/html")
    msg.send()


def send_processed_notification(order_id):
    """Send a notification that the order is processed."""

    order = Order.objects.get(id=order_id)

    date = order.date_processed.strftime('%Y-%m-%d %H:%M:%S')

    title = 'Ваше замовлення надіслано!'
    message = get_template('books/messages/notify_processed.txt')
    context = {
        'book': order.book, 'id': order.id,
        'quantity': order.quantity,
        'authors': order.book.show_authors,
        'date': date, 'title': title
        }
    body = message.render(context)

    html_message = render_to_string('books/messages/notify_processed.html',
                                    context)
    msg = EmailMultiAlternatives(
            title,
            body,
            settings.EMAIL_HOST_USER,
            [order.email],
            )
    msg.attach_alternative(html_message, "text/html")
    msg.send()
