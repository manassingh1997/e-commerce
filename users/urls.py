from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView, LogoutView, DashboardView

urlpatterns = [
 path('auth/register', RegisterView.as_view(), name="auth_register"),
 path('auth/login',LoginView.as_view(), name="auth_login"),
 path('auth/logout',LogoutView.as_view(), name="auth_logout"),
 path('token', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
 path('token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),  
 path('dashboard',DashboardView.as_view(), name = 'dashboard') 
]