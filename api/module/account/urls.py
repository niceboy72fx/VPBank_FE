from django.urls import path, include

from module.account.views import AccountView, LoginUserView, LogoutApiView, RegisterUserView, VerifyUserEmail
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)
from rest_framework.routers import DefaultRouter

authpatterns =[
    path("register/", RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    # path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
    path('logout/', LogoutApiView.as_view(), name='logout')
]

# accounts = [
#     path("", Account, name="all"),
# ]

router = DefaultRouter()
router.register('account', AccountView, basename='account')

urlpatterns = [
    path("auth/", include(authpatterns)),
    # path("account/", AccountView.as_view()),
]