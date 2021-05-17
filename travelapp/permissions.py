from rest_framework import permissions


class OwnsOrIsInstructorOrReadOnly(permissions.BasePermission):
    """
    Класс permissions, который разрешает редактировать объекты только Гидам.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return request.user.is_instructor

    def has_object_permission(self, request, view, obj):
        return request.user.is_instructor and obj.instructor == request.user.instructor
