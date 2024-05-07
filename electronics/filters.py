from django_filters import rest_framework
from electronics.models import Seller


class SellerFilter(rest_framework.FilterSet):
    contact__country = rest_framework.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Seller
        fields = ['contact__country', ]
