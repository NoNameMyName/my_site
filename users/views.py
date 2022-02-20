from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
