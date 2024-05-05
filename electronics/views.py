from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from electronics.models import Seller
from electronics.permissions import IsActive
from electronics.serializers import SellerSerializer, SellerUpdateSerializer


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
            queryset = queryset.filter(country=country)
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
            permission_classes = [IsAuthenticated, IsOwner, ]
        return [permission() for permission in permission_classes]
