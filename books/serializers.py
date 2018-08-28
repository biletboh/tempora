from rest_framework import serializers

from .models import Order
from .utils import send_order_notification


class OrderSerializer(serializers.ModelSerializer):
    """Serialize order data."""

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'message', 'quantity', 'book',
                  'address')

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        send_order_notification(order.id)
        return order
