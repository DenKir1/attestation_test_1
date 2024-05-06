from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from electronics.models import Seller
from electronics.permissions import IsActive
from electronics.serializers import SellerSerializer, SellerUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Продуктов
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ('retrieve', 'list', 'create'):
            permission_classes = [IsAuthenticated, ]
        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAdmin, ]
        return [permission() for permission in permission_classes]


class ContactViewSet(viewsets.ModelViewSet):
    """
    Контроллер для модели Контактов
    """

    queryset = Contact.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ('retrieve', 'list', 'create'):
            permission_classes = [IsAuthenticated, ]
        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAdmin, ]
        return [permission() for permission in permission_classes]


class SellerViewSet(ModelViewSet):
    # queryset = Seller.objects.all()
    # serializer_class = SellerSerializer
    permission_classes = [IsActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country', ]
    filterset_fields = ['contact__country', ]

    def get_queryset(self):
        queryset = Seller.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            contacts = Contact.filter(country=country)
            queryset = queryset.filter(contact=[contacts]) # examine
        return queryset

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return SellerSerializer
        if self.action in ('update', 'partial_update'):
            return SellerUpdateSerializer
        return SellerSerializer

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ('retrieve', 'list'):
            permission_classes = [IsAuthenticated, ]
        if self.action in ('update', 'destroy', 'partial_update'):
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin, ]
        return [permission() for permission in permission_classes]


# filter to file
import django_filters
class SellerFilter(django_filters.FilterSet):
    contact__country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    class Meta:
        model = Seller
        fields = ['contact__country']
