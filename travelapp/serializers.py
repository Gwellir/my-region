from rest_framework import serializers
from travelapp.models import Route, Trip


class RouteSerializer(serializers.ModelSerializer):
    featured_thumb = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = ['id', 'name', 'route_type', 'short_desc', 'long_desc',
                  'location', 'duration', 'length', 'complexity',
                  'featured_photo', 'featured_thumb']

    def get_featured_thumb(self, obj):
        rq = self.context.get('request')
        return rq.build_absolute_uri(obj.featured_thumb.url)


class RouteRetrieveSerializer(RouteSerializer):
    trips = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()

    class Meta:
        model = RouteSerializer.Meta.model
        fields = RouteSerializer.Meta.fields + ['photos', 'trips']

    def get_trips(self, obj):
        return [trip.id for trip in obj.trips.all()]

    def get_photos(self, obj):
        rq = self.context.get('request')
        return [{
            'id': photo.id,
            'thumb_url': rq.build_absolute_uri(photo.image_thumb.url),
            'url': rq.build_absolute_uri(photo.image.url),
        } for photo in obj.photos.all()]


class TripSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.id')
    kids = serializers.ReadOnlyField()
    adults = serializers.ReadOnlyField()

    class Meta:
        model = Trip
        fields = ['id', 'route', 'price', 'starts_at', 'ends_at', 'instructor',
                  'kids', 'adults', 'max_group_size', 'options']
