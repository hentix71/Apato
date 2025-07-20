from rest_framework.permissions import BasePermission

class IsHost(BasePermission):
    """Custom logic so only the host can create the listing"""
    def has_permission(self, request, view):
        """Has permission is for view level access level"""
        user = request.user

        """user must be host, is authenticated and user"""
        return bool(user and user.is_authenticated and user.is_host)