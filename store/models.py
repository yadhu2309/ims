from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    product = models.ManyToManyField(Product)
