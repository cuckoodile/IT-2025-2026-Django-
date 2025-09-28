# permissions.py (custom permissions for restrictions)
from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Allows teachers to modify subjects, students/admins to read.
    For subjects: Only the assigned teacher can edit/delete.
    """
    def has_object_permission(self, request, view, obj): # type: ignore
        if request.method in permissions.SAFE_METHODS:
            return True
        # For write methods, check if user is the teacher of the subject
        if hasattr(request.user, 'teacher_profile'):
            return obj.teacher == request.user.teacher_profile
        return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    For profiles like Student/Teacher: Only the user themselves can edit.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Assuming obj has 'user' field
        return obj.user == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    For courses/subjects creation: Admins only, or custom logic.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff