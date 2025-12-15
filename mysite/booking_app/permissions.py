from rest_framework import permissions


class IsClientForBooking(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if view.__class__.__name__ in ['BookingView', 'ReviewView']:
            return getattr(request.user, 'user_role', None) == 'client'
        return True



class CreateHotelPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'owner'