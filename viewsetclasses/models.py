from django.db import models

from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=50)
    drug_category = models.ForeignKey('DrugCategory', on_delete=models.CASCADE, related_name='drugs')
    use_by_date = models.DateField()
    delivered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class DrugCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Drug categories'

    def __str__(self):
        return self.name


GENDER_CHOICES = (('m', 'male'), ('f', 'female'))


class Patient(models.Model):
    name = models.CharField(max_length=150, default='', blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='m')
    age = models.IntegerField()
    admited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

