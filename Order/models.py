from django.db import models
from MainPage.models import Products
from django.core.validators import RegexValidator
# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='orderItem')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):

        return f'{self.product}'



class Order(models.Model):
    product = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='orderItem')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True)
    address = models.CharField(max_length=225)
    reference_point = models.CharField(max_length=225)
    comments = models.CharField(max_length=225)
    def __str__(self):
        return f'{self.product}'