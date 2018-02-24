from django import forms
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    """Provide Contact Form."""

    name_error = {'required': _('Будь ласка, уведіть ваше ім’я.')}
    email_error = _('Будь ласка, уведіть ваш емайл.')
    email_invalid = _('Будь ласка, уведіть коректну емeйл адресу.')
    phone_error = _('Будь ласка, уведіть номер вашого телефону.')
    phone_invalid = _(
                    """Будь ласка, уведіть коректний номер телефону.
                    Наприклад, +380XXXXXXXXX."""
                    )
    message_error = _('Будь ласка, уведіть повідомлення.')

    name = forms.CharField(
                        error_messages=name_error,
                        label=_("Ім'я"), max_length=80,
                        )
    email = forms.EmailField(
                            label=_('Емейл'), max_length=100,
                            error_messages={
                                        'required': email_error,
                                        'invalid': email_invalid,
                                        },
                            )
    phone = PhoneNumberField(
                            label=_('Телефон +380XXXXXXXXX'),
                            error_messages={
                                        'required': phone_error,
                                        'invalid': phone_invalid,
                                        },
                            )
    message = forms.CharField(
                        label=_('Повідомлення'), max_length=1000,
                        widget=forms.Textarea(attrs={'rows': '5'}),
                        error_messages={'required': message_error},
                        required=True,
                        )


class BookOrderForm(ContactForm):
    book_id = forms.IntegerField(label=_("ID книги"))
