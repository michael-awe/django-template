from django.urls import path, include
from . import views

app_name = "landing_page"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/movies", views.search_movies, name="search_movies")
]
