from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import OrderItem
from .serializers import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import AllowAny

class OrderItemView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer



class OrderItemListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class =  OrderSerializer
    permission_classes = [AllowAny, ]


class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer