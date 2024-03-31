from django.db import models
from django.contrib.postgres.fields import ArrayField
from .choices import *


class Movie(models.Model):
    name = models.CharField(max_length=30, unique=False)
    genre = models.CharField(max_length=13, unique=False, choices=GENRES)
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    language = models.CharField(max_length=30, unique=False, choices=LANGUAGES)

    # people
    top_cast = ArrayField(models.CharField(max_length=60, unique=False))
    directors = ArrayField(models.CharField(max_length=60, unique=False))
    writers = ArrayField(models.CharField(max_length=60, unique=False))
    cinematographer = ArrayField(models.CharField(max_length=60, unique=False))
    composer = ArrayField(models.CharField(max_length=60, unique=False))


class Recommendation(models.Model):
    genre = models.CharField(max_length=13, unique=False, choices=GENRES)
    year_span = models.PositiveIntegerField(choices=YEAR_SPANS)
