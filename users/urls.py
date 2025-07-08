from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, DeleteAccountView, LogoutView,UserProfileUpdateView, PasswordChangeView, RequestPasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete_account'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),


    path('change-pasword/', PasswordChangeView.as_view(), name='user-change-password'),
    path("password-reset/", RequestPasswordResetView.as_view(), name="request-password-reset"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
]
