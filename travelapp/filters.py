from django_filters import rest_framework as filters

from travelapp.models import Trip


class TripFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    starts_after = filters.DateTimeFilter(field_name="starts_at", lookup_expr="gte")
    starts_before = filters.DateTimeFilter(field_name="starts_at", lookup_expr="lte")
    ends_after = filters.DateTimeFilter(field_name="ends_at", lookup_expr="gte")
    ends_before = filters.DateTimeFilter(field_name="ends_at", lookup_expr="lte")
    # by route filters
    region = filters.NumberFilter(field_name="route", lookup_expr="location")
    district = filters.NumberFilter(
        field_name="route", lookup_expr="location__district"
    )
    route_type = filters.NumberFilter(field_name="route", lookup_expr="route_type")
    complexity = filters.NumberFilter(field_name="route", lookup_expr="complexity")
    min_duration = filters.NumberFilter(field_name="route", lookup_expr="duration__gte")
    max_duration = filters.NumberFilter(field_name="route", lookup_expr="duration__lte")

    class Meta:
        model = Trip
        fields = [
            "min_price",
            "max_price",
            "starts_after",
            "starts_before",
            "ends_after",
            "ends_before",
            "instructor",
            # by route
            "route",
            "region",
            "district",
            "route_type",
            "complexity",
            "min_duration",
            "max_duration",
        ]
