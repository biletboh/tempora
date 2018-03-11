from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serialize order data."""

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'message', 'quantity', 'book')
