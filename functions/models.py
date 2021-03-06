from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=20)
    number = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name


class Herb(models.Model):
    name = models.CharField(max_length=20)
    number = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
