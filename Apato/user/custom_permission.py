from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """Custom logic for the Owner or Admin only permission"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff == True or request.user.id == obj.id:
            """Either the "is_staff" admin or the owner of the object(User instance filtered from lookup field)"""
            return True
        else:
            return False