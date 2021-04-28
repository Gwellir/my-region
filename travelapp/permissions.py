from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class OwnsOrIsInstructorOrReadOnly(permissions.BasePermission):
    """
    Класс permissions, который разрешает редактировать объекты только Гидам.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        if request.method == "POST":
            return request.user.is_instructor
        else:
            return (
                request.user.is_instructor and obj.instructor == request.user.instructor
            )
