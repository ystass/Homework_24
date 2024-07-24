from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
