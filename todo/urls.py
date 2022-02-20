from rest_framework import routers

from .views import TodoViewSet


router = routers.DefaultRouter()
router.register(prefix='api/v1/todo', viewset=TodoViewSet, basename='todo')

urlpatterns = router.urls
