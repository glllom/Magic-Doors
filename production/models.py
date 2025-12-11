from django.db import models

"""Product models"""

class ProductClass(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductFamily(models.Model):
    name = models.CharField(max_length=20)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    product_family = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PresetGroup(models.Model):
    name = models.CharField(max_length=20)


class Preset(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    preset_group = models.ForeignKey(PresetGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Preset for {self.product}"



"""Elements"""
class Engraving(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Window(models.Model):
    name = models.CharField(max_length=20)

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

