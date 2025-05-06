from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Admins can view & edit. Employees can only view.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        # Allow all authenticated users to read
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True

        # Only allow write if user is admin
        return user.role == 'admin'
