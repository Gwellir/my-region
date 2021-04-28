from django.urls import path

import userapp.views as userapp

app_name = "userapp"

urlpatterns = [
    path("instructors/", userapp.InstructorList.as_view(), name="instructor_list"),
    # path('create/', userapp..as_view(), name='user_create'),
    path(
        "traveler_details/<int:pk>/",
        userapp.TravelerDetailView.as_view(),
        name="traveler_details",
    ),
    path(
        "instructor_details/<int:pk>/",
        userapp.InstructorDetailView.as_view(),
        name="instructor_details",
    ),
    path(
        "traveler_profile/",
        userapp.TravelerProfileView.as_view(),
        name="traveler_profile",
    ),
    path(
        "instructor_profile/",
        userapp.InstructorDetailView.as_view(),
        name="instructor_profile",
    ),
]
