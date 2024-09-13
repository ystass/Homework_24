from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from users.models import Payments
from users.serialiser import PaymentsSerializer


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
