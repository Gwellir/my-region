from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Класс permissions, которые разрешает работать с данными профиля только самим юзерам.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        else:
            return request.user == obj
