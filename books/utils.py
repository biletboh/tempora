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
        'book': order.book, 'id': order.id, 'date': date
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
