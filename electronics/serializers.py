from rest_framework import serializers
from electronics.models import Seller, Product, Contact


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SellerViewSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    contact = ContactSerializer(required=False)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('owner', )


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('debt', 'created', 'owner', )
