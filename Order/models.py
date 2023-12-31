from django.db import models
from MainPage.models import Products
from django.core.validators import RegexValidator
from  account.models import MyUser
# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='orderItem')
    quantity = models.PositiveIntegerField(default=1)

    def get_sale(self):
        price = self.product.price
        total = int(price * self.quantity)
        return total
    def __str__(self):

        return f'{self.product}'




# оформление заказа


class OrderSuccess(models.Model):

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_item')
    order_number = models.CharField(max_length=225, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True)
    address = models.CharField(max_length=225)
    reference_point = models.CharField(max_length=225)
    comments = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.product}'








