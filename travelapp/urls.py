from django.urls import path

import travelapp.views as travelapp

app_name = "travelapp"

urlpatterns = [
    path("", travelapp.TripSelectorList.as_view(), name="trip_selector"),
    path("routes/", travelapp.RouteList.as_view(), name="route_list"),
    path("route/create/", travelapp.RouteCreateView.as_view(), name="route_create"),
    path("route/<int:pk>/", travelapp.RouteDetail.as_view(), name="route_read"),
    path("trip/<int:pk>", travelapp.TripDetail.as_view(), name="trip_read"),
]
