from django.db import models


class ADS(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.SmallIntegerField()
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    name = models.CharField(max_length=200)


def __str__(self):
    return self.slug
