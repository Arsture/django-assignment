from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def is_admin(self, request):
        return request.user and request.user.is_staff

    def has_permission(self, request, view):
        return self.is_admin(request)

    def has_object_permission(self, request, view, obj):
        return self.is_admin(request)


class IsAuthenticated(IsAdmin):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True

        if request.method == 'POST':
            return request.user and request.user.is_authenticated


class IsOwner(IsAdmin):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True

        if request.method in ['PUT', 'DELETE', 'PATCH']:
            return True

    def has_object_permission(self, request, view, obj):
        if super().has_object_permission(request, view, obj):
            return True

        return obj.created_by == request.user
