from rest_framework import permissions

class IsClientForBooking(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if view.basename in ['booking', 'review']:
            return request.user.user_role == 'client'
        return True

class IsOwnerForHotel(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.role == 'owner':
            return obj.owner == request.user
        return False

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.user_role == 'owner'