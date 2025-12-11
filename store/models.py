from django.db import models



"""Material"""

class SheetMaterial(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class LineMaterial(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



"""Furniture"""

class Lock(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Furniture(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Hinge(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Handle(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

