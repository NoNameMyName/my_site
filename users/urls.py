from rest_framework import routers

from .views import TodoViewSet


router = routers.DefaultRouter()
router.register(prefix='api/v1/users', viewset=TodoViewSet, basename='users')

urlpatterns = router.urls