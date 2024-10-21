from rest_framework import permissions

class IsCopyAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='CopyAdmin').exists():
            return True
        return False

class IsCopyReadOnlyUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS
        return False
