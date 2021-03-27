from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class OwnsOrIsTravelerOrReadOnly(permissions.BasePermission):
    """
    Класс permissions, который разрешает редактировать объекты только путешественникам.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_traveler
        else:
            return request.user.is_traveler and obj.traveler == request.user.traveler