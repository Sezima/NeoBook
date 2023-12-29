from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


from rest_framework import generics
from .models import OrderItem, OrderSuccess
from .serializers import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsDepartmentAuthor


class OrderItemView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated, ]




class OrderItemListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class =  OrderSerializer
    permission_classes = [AllowAny, ]


class OrderView(generics.CreateAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

class OrderSuccessView(generics.CreateAPIView):
    queryset = OrderSuccess.objects.all(),
    serializer_class = OrderItemSerializer

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsDepartmentAuthor, ]
        else:
            permissions = []
        return [permission() for permission in permissions]
