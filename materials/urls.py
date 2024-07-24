from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet, basename="courses")

urlpatterns = []

urlpatterns += router.urls
