from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Класс permissions, которые разрешает работать с данными профиля только самим юзерам.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        else:
            return request.user == obj
