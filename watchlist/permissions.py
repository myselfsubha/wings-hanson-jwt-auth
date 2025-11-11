from rest_framework import permissions

class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.reviewed_user == request.user or request.user.is_staff  #it means that only the user who created the review or the admin can edit the review