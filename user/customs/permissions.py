from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 1:
            return True
        return False


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 2:
            return True
        return False
