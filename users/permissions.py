from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    massage = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
