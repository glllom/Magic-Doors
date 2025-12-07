from django.db import models

"""Product models"""

class ProductClass(models.Model):
    name = models.CharField(max_length=20)

class ProductFamily(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=20)



class Order(models.Model):
    number = models.IntegerField()

class Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


