from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # anyone can read
        if request.method in SAFE_METHODS:
            return True

        # only owner can modify
        return obj.seller == request.user
