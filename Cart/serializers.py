
from rest_framework import serializers
from .models import Cart, CartItem
from MainPage.serializers import ProductsSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']