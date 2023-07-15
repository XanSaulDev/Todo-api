from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        has_permission = super().has_permission(request, view)
        if not has_permission:
            raise PermissionDenied({"errors": [_("You are not authenticated.")]})
        return has_permission