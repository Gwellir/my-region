from rest_framework import serializers
from travelapp.models import Route, Trip


class RouteSerializer(serializers.ModelSerializer):
    trips = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = ['id', 'name', 'route_type', 'short_desc', 'long_desc',
                  'location', 'duration', 'length', 'complexity',
                  'featured_photo', 'trips', 'photos']

    def get_trips(self, obj):
        return [trip.id for trip in obj.trips.all()]


class TripSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.id')
    kids = serializers.ReadOnlyField()
    adults = serializers.ReadOnlyField()

    class Meta:
        model = Trip
        fields = ['id', 'route', 'price', 'starts_at', 'ends_at', 'instructor',
                  'kids', 'adults', 'max_group_size', 'options']
