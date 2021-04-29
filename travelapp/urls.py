from django.urls import include, path
from rest_framework.routers import DefaultRouter

import travelapp.views as travelapp

app_name = "travelapp"

urlpatterns = [
    path("", travelapp.TripSelectorList.as_view(), name="trip_selector"),
    path("routes/", travelapp.RouteList.as_view(), name="route_list"),
    path("route/create/", travelapp.RouteCreateView.as_view(), name="route_create"),
    path("route/<int:pk>/", travelapp.RouteDetail.as_view(), name="route_read"),
    # path('route/update/<int:pk>/', travelapp.RouteUpdate.as_view(), name='route_update'),
    # path('route/delete/<int:pk>/', travelapp.RouteDelete.as_view(), name='route_delete'),
    path("trip/<int:pk>", travelapp.TripDetail.as_view(), name="trip_read"),
]
