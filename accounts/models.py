from django.db import models
from django.contrib.auth.models import AbstractUser
from recommendations.models import Movie


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    friends = models.ManyToManyField("User", blank=True)

    # external accounts, used for connections
    letterboxd_username = models.CharField(
        max_length=15, unique=True, null=True, blank=True
    )
    imdb_user_id = models.CharField(max_length=32, unique=True, null=True, blank=True)

    # 'Movie' connections - movies already seen and movies already recommended
    seen_films = models.ManyToManyField(Movie, related_name="users_seen", blank=True)
    recommended_films = models.ManyToManyField(
        Movie, related_name="users_recommended", blank=True
    )
