from rest_framework import serializers
from Order.models import OrderItem, OrderSuccess
from MainPage.models import  Products


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'get_sale')



class OrderItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderSuccess
        fields = '__all__'

