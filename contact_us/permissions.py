from rest_framework import permissions

class IsObjectOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.contact == request.user
