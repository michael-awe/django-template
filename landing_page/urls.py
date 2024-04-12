from django.urls import path, include
from . import views

app_name = "landing_page"

urlpatterns = [
    path("", views.index, name="index"),
    path("get-csrf-token/", views.get_csrf_token, name="get_csrf_token"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/movies", views.search_movies, name="search_movies"),
    path("movie/", views.movie, name="movie"),
    path("api/search/movies", views.search_movies_json, name="search_movies_json"),
]
