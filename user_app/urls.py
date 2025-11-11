from django.urls import path
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    # TokenBlacklistView
)
from user_app.views import LoginApiView, RegistrationView, Logout

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='token_obtain_pair'),
    path('register/',RegistrationView.as_view(), name='register'),
    path('logout/',Logout.as_view(),name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]