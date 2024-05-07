from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsAdmin, IsUser
from users.serializers import UserSerializer, MyTokenObtainPairSerializer, UserUpdateSerializer, UserCreateSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ('retrieve', 'list'):
            permission_classes = [IsAuthenticated, IsAdmin, ]
        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAuthenticated, IsUser | IsAdmin, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserUpdateSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
