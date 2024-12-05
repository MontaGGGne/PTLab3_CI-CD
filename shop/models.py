from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=100)
    max_quantity = models.PositiveIntegerField(default=100)
    growth_percentage = models.PositiveIntegerField(default=0)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=1)
    # order_amount = models.PositiveIntegerField(default=0)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)