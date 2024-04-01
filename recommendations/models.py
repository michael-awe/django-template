from django.db import models
from django.contrib.postgres.fields import ArrayField
from .choices import *


class Movie(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=13, choices=GENRES)
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    language = models.CharField(max_length=30, choices=LANGUAGES)

    # people
    top_cast = ArrayField(models.CharField(max_length=60))
    directors = ArrayField(models.CharField(max_length=60))
    writers = ArrayField(models.CharField(max_length=60))
    cinematographer = ArrayField(models.CharField(max_length=60))
    composer = ArrayField(models.CharField(max_length=60))

    uh = ArrayField(models.CharField(max_length=60, choices=TRIGGERS))
    watch_providers = ArrayField(models.CharField(max_length=60))
    tmdb_keywords = ArrayField(models.CharField(max_length=60))
    tmdb_id = models.PositiveIntegerField()


class Recommendation(models.Model):
    genre = models.CharField(max_length=13, , choices=GENRES)
    year_span = models.PositiveIntegerField(choices=YEAR_SPANS)
