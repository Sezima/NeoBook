from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', blank=True, null=True)



class Products(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # выбор штук надо реализовать
    def __str__(self):
        return self.title


