from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import OrderItem
from .serializers import OrderItemSerializer

class OrderItemView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
