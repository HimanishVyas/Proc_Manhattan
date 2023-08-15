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

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class WriteOnly(BasePermission):
    def has_permission(self, request, view):
        WRITE_METHODS = [
            "POST",
        ]
        return request.method in WRITE_METHODS


class ExceptDelete(BasePermission):
    message = "dont allow for delete"

    def has_permission(self, request, view):
        WRITE_METHODS = [
            "DELETE",
        ]
        return request.method not in WRITE_METHODS


class DeleteOnly(BasePermission):
    def has_permission(self, request, view):
        DELETE_METHODS = [
            "DELETE",
        ]
        return request.method in DELETE_METHODS


class UpdateOnly(BasePermission):
    def has_permission(self, request, view):
        UPDATE_METHODS = [
            "UPDATE",
        ]
        return request.method in UPDATE_METHODS
