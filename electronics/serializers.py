from rest_framework import serializers
from electronics.models import Seller


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    contact = ContactSerializer(many=True, required=False)
    class Meta:
        model = Seller
        fields = '__all__'


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('debt', 'created', )
