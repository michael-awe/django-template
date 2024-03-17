from django.db import models
from django.contrib.auth.models import AbstractUser
from recommendations.models import Movie


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    friends = models.ManyToManyField("User", blank=True)
    letterboxd_username = models.CharField(max_length=15, unique=True, null=True)
    imdb_user_id = models.CharField(max_length=32, unique=True, null=True)
    seen_films = models.ManyToManyField(Movie, related_name="users_seen", blank=True)
