from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Cart, CartItem
from MainPage.serializers import ProductsSerializer
from .serializers import CartItemSerializer, CartSerializer

# Create your views here.
class CartView(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart

class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('pk')
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        serializer.save(cart=cart, product=product, quantity=self.request.data.get('quantity', 1))

class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        product_id = self.kwargs.get('pk')
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        return CartItem.objects.get(cart=cart, product_id=product_id)