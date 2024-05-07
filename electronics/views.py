from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from electronics.filters import SellerFilter
from electronics.models import Seller, Product, Contact
from users.permissions import IsActive, IsAdmin, IsOwner
from electronics.serializers import SellerSerializer, SellerUpdateSerializer, ProductSerializer, ContactSerializer, \
    SellerViewSerializer


class ProductViewSet(ModelViewSet):
    """
    Контроллер для модели Продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permission_classes = [IsActive, ]

        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAdmin, ]
        return [permission() for permission in permission_classes]


class ContactViewSet(ModelViewSet):
    """
    Контроллер для модели Контактов
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        permission_classes = [IsActive, ]

        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAdmin, ]
        return [permission() for permission in permission_classes]


class SellerViewSet(ModelViewSet):
    """
        Контроллер для модели Объекта торговой сети
    """
    queryset = Seller.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SellerFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return SellerViewSerializer
        if self.action in ('update', 'partial_update'):
            if self.request.user.is_staff:
                return SellerSerializer
            return SellerUpdateSerializer
        return SellerSerializer

    def get_permissions(self):
        permission_classes = [IsActive, ]
        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsOwner | IsAdmin, ]
        return [permission() for permission in permission_classes]
