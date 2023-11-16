from rest_framework.permissions import BasePermission

from users.models import Roles


class IsModerator(BasePermission):
    massage = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.role == Roles.MODERATOR:
            return True

        return False


class IsOwner(BasePermission):
    massage = 'Вы не являетесь пользователем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        return False


class IsSubscriber(BasePermission):
    massage = 'Вы не являетесь подписчиком!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        return False