from rest_framework import serializers
from electronics.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('debt', 'created', )
