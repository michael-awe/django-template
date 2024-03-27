from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30, unique=False)
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=60, unique=False)
