from django.db import models
from django.core.validators import MinValueValidator
import django_filters
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', blank=True, null=True)


    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)]);
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    # выбор штук надо реализовать


    def __str__(self):
        return f"{self.title} ({self.category})"

# фильтрация
class ProductsFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains', required=True)

    class Meta:
        model = Products
        fields = ['category']
# order-create
