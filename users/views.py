from rest_framework.generics import ListAPIView, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Subscription
from materials.serializer import SubscriptionSerializer
from users.models import Payments, User
from users.serialiser import PaymentsSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "course",
        "lesson",
    )
    ordering_fields = ("date",)
    search_fields = ("payment_method",)


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user  # получаем пользователя из self.requests
        course_id = self.request.data.get('course')  # получаем id курса из self.reqests.data
        course = get_object_or_404(Course, pk=course_id)  # получаем объект курса из базы с помощью get_object_or_404
        sub_item = Subscription.objects.all().filter(user=user).filter(course=course)  # получаем объекты подписок по текущему пользователю и курса

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if sub_item.exists():
            sub_item.delete()
            message = 'Подписка отключена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка включена'
        # Возвращаем ответ в API
        return Response({"message": message})
