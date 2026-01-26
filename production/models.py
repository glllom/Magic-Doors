from django.db import models

"""Product models"""
"""main group of products"""
class ProductFamily(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=20)
    product_family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=20)
    product_family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)
    sku = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class ProductSeries(models.Model):
    name = models.CharField(max_length=20)

class ProductModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    sku = models.CharField(max_length=20, unique=True)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE)

class ProductModelBOM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    sku = models.CharField(max_length=20, unique=True)



"""Elements"""

class Engraving(models.Model):
    name = models.CharField(max_length=20)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Window(models.Model):
    name = models.CharField(max_length=20)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LockPocket(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HingePocket(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ExtraPocket(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

