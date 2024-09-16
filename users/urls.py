from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPIView

app_name = UsersConfig.name
router = SimpleRouter()
#router.register("", UserViewSet, basename="users")


urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(), name="payments"),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    )
]
urlpatterns += router.urls
