from rest_framework import serializers
from Order.models import Order , OrderItem
from MainPage.models import  Products


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())

    class Meta:
        model = OrderItem
        fields =  '__all__'



class OrderItemSerializer(serializers.ModelSerializer):

    product = serializers.IntegerField(source='product.id')  # Assuming 'product' is a ForeignKey to Product

    class Meta:
        model = Order
        fields = '__all__'