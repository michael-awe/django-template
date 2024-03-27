from django.urls import path, include
from . import views

app_name = "landing_page"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/movies", views.search_movies, name="search_movies"),
]
