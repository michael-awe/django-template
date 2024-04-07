from django.db import models
from django.contrib.postgres.fields import ArrayField
from .choices import *


class Movie(models.Model):
    name = models.CharField(max_length=80)
    genres = ArrayField(models.CharField(max_length=13, choices=GENRES))
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    language = models.CharField(max_length=2, choices=LANGUAGES)
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

    watch_providers = ArrayField(models.CharField(max_length=60, choices=STREAMING))
    keywords = ArrayField(models.CharField(max_length=60))
    tmdb_id = models.PositiveIntegerField()
    imdb_rating = models.DecimalField(max_digits=10, decimal_places=2)
    imdb_votes = models.PositiveIntegerField()


class Recommendation(models.Model):
    possible_films = models.ManyToManyField("Movie", related_name="recommendations")
    possible_film_count = models.PositiveIntegerField()

    # answers
    genre = ArrayField(models.CharField(max_length=13, choices=GENRES))
    year_span = models.PositiveIntegerField(choices=YEAR_SPANS)
    runtime_span = models.PositiveIntegerField(choices=RUNTIME_SPANS)
    languages = ArrayField(models.CharField(max_length=2, choices=LANGUAGES))
    triggers = ArrayField(models.CharField(max_length=100, choices=TRIGGERS))
    watch_providers = ArrayField(models.CharField(max_length=60, choices=STREAMING))

    preferred_cast = ArrayField(models.CharField(max_length=60))
    preferred_crew = ArrayField(models.CharField(max_length=60))
    excluded_cast = ArrayField(models.CharField(max_length=60))
    excluded_crew = ArrayField(models.CharField(max_length=60))

    popular = models.BooleanField(default=False)
    well_reviewed = models.BooleanField(default=True)
    external_account_influence = models.BooleanField(default=False)

    # TODO jokey questions
