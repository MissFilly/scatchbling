from django.db import models
from django.core.validators import MinValueValidator


class Size(models.Model):
    name = models.CharField(max_length=2, unique=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cost = models.FloatField(validators=[MinValueValidator(0)])
    sizes = models.ManyToManyField(Size)

    def __unicode__(self):
        return '{} - ${}'.format(self.name, self.cost)