from django.urls import include, path

import authapp.views as authapp

app_name = "authapp"

urlpatterns = [
    path("login/", authapp.login_view, name="login"),
    path("logout/", authapp.logout, name="logout"),
    path("", include("django.contrib.auth.urls")),
    # path('edit/', authapp.edit, name='edit'),
    path("signup/", authapp.RegisterView.as_view(), name="register"),
    path("signup_api/", authapp.APIRegisterView.as_view(), name="api_register"),
    path(
        "signup/traveler/", authapp.TravelerSignupView.as_view(), name="signup_traveler"
    ),
    path(
        "signup/instructor/",
        authapp.InstructorSignupView.as_view(),
        name="signup_instructor",
    ),
    path("verify/<str:email>/<str:activation_key>/", authapp.verify, name="verify"),
]
