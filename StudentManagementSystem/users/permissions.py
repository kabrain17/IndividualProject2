from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    """Разрешение только для студентов"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Student'

class IsTeacher(BasePermission):
    """Разрешение только для учителей"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Teacher'

class IsAdmin(BasePermission):
    """Разрешение только для администраторов"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'
