from django.urls import path

import ordersapp.views as ordersapp

app_name = "ordersapp"

urlpatterns = [
    # path('', travelapp.RouteList.as_view(), name='route_list'),
    path("create/<int:pk>", ordersapp.OrderCreate.as_view(), name="create_order"),
    # path('route/<int:pk>/', travelapp.RouteDetail.as_view(), name='route_read'),
    # path('route/update/<int:pk>/', travelapp.RouteUpdate.as_view(), name='route_update'),
    # path('route/delete/<int:pk>/', travelapp.RouteDelete.as_view(), name='route_delete'),
    # path('trip/<int:pk>', travelapp.TripDetail.as_view(), name='trip_read'),
]
