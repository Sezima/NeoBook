from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

from .models import *
from .serializers import CategorySerializer, ProductsSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


class ProductsListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductsFilter

    def get_queryset(self):
        queryset = Products.objects.all()
        category_param = self.request.query_params.get('category', None)

        if category_param:
            queryset = queryset.filter(category__name__icontains=category_param)

        return queryset






