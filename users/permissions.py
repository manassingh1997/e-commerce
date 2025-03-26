from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    # Custom permission to allow only sellers to access certain views.
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'
    
class IsBuyer(permissions.BasePermission):
    # Custom permission to allow only buyers to access centain views.
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'buyer'