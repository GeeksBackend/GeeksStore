from django.urls import path
from rest_framework.routers import DefaultRouter 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPI

router = DefaultRouter()
router.register('users', UserAPI, "api_users")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_users_login"),
    path('login/refresh/', TokenRefreshView.as_view(), name="api_users_refresh"),
]

urlpatterns += router.urls