from django.urls import path

from socialapp import views as socialapp

app_name = "socialapp"

urlpatterns = [
    path(
        "trip_comment/create/<int:pk>",
        socialapp.TripCommentCreate.as_view(),
        name="trip_comment_create",
    ),
]
