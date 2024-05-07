from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    message = "Вы неактивны"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active


class IsAdmin(BasePermission):
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        return request.user.is_staff


class IsUser(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
