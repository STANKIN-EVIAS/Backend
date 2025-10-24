from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Право доступа, разрешающее доступ только владельцу объекта или администратору.
    """
    def has_object_permission(self, request, view, obj):
        # Администраторы могут всё
        if request.user.is_staff:
            return True
        
        # Проверяем, является ли пользователь владельцем
        return obj.id == request.user.id


class IsVetOrAdmin(permissions.BasePermission):
    """
    Право доступа для ветеринаров и администраторов.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'vet' or request.user.is_staff
        )