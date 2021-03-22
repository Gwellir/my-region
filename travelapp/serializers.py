from rest_framework import serializers
from travelapp.models import Route, Trip


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ['id', 'name', 'route_type', 'short_desc', 'long_desc',
                  'location', 'duration', 'length', 'complexity',
                  'featured_photo', 'trips']


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['id', 'route', 'price', 'starts_at', 'ends_at', 'instructor',
                  'kids', 'adults', 'max_group_size', 'options']