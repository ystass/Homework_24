from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserViewSet, PaymentsCreateAPIView

app_name = UsersConfig.name
router = SimpleRouter()
router.register("", UserViewSet, basename="users")


urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(permission_classes=(AllowAny,)), name="payments"),
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='create-payment'),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    )
]
urlpatterns += router.urls
