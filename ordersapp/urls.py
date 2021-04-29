from django.urls import path

import ordersapp.views as ordersapp

app_name = "ordersapp"

urlpatterns = [
    path("create/<int:pk>", ordersapp.OrderCreate.as_view(), name="create_order"),
]
