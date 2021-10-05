from django.utils import timezone

from rest_framework import serializers

from .models import Order
from .utils import (
    send_order_notification,
    send_received_notification,
    send_processed_notification,
)


class OrderSerializer(serializers.ModelSerializer):
    """Serialize order data."""

    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "message",
            "quantity",
            "book",
            "address",
        )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        send_order_notification(order.id)
        send_received_notification(order.id)
        return order


class OrderProcessingSerializer(serializers.ModelSerializer):
    """Serialize data for order processing."""

    notification = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Order
        fields = ("processed", "notification")

    def update(self, instance, validated_data):
        instance.processed = validated_data.get(
            "processed", instance.processed
        )
        instance.date_processed = timezone.now()
        instance.save()

        notification = validated_data.get("notification", False)
        if notification:
            send_processed_notification(instance.id)

        return instance
