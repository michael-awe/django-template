from django.db import models
from django.contrib.postgres.fields import ArrayField
from .choices import *


class Movie(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=13, choices=GENRES)
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    language = models.CharField(max_length=30, choices=LANGUAGES)
    budget = models.PositiveIntegerField(default=0)
    revenue = models.PositiveIntegerField(default=0)

    poster = models.TextField()
    overview = models.TextField()
    tagline = models.TextField()

    # people
    starring = ArrayField(models.CharField(max_length=60))
    director = ArrayField(models.CharField(max_length=60))
    writer = ArrayField(models.CharField(max_length=60))
    cinematographer = ArrayField(models.CharField(max_length=60))
    composer = ArrayField(models.CharField(max_length=60))

    watch_providers = ArrayField(models.CharField(max_length=60))
    keywords = ArrayField(models.CharField(max_length=60))
    tmdb_id = models.PositiveIntegerField()
    imdb_rating = models.DecimalField(max_digits=10, decimal_places=2)
    imdb_votes = models.PositiveIntegerField()


class Recommendation(models.Model):
    genre = models.CharField(max_length=13, choices=GENRES)
    year_span = models.PositiveIntegerField(choices=YEAR_SPANS)
