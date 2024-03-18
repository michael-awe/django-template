from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/create/", views.create_movie, name="create_movie"),
    path("movies/<int:movie_id>/delete/", views.delete_movie, name="delete_movie"),
    path("movies/<int:movie_id>/update/", views.update_movie, name="update_movie"),
]
