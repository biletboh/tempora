from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def send_contact_message(name, email, phone, message):
    content = get_template('pbhouse/messages/contact.txt')
    context = { 
            'name': name, 'email': email,
            'phone': phone, 'message': message}
    body = content.render(context)
    msg = EmailMessage(
            'Tempora: зворотній зв’язок.',
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            )
    msg.send()

