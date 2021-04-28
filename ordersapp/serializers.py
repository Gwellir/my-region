from rest_framework import serializers

from ordersapp.models import OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "traveler",
            "trip",
            "adults_amount",
            "kids_amount",
            "options_used",
            "contact_phone",
            "contact_email",
            "notes",
        ]
