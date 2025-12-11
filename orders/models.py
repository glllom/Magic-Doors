from django.db import models
from production.models import Product

"""Orders & Items"""
class Order(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"Order #{self.number}"

class Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Item #{self.number} in {self.order}"



