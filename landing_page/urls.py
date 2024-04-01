from django.urls import path, include
from . import views

app_name = "landing_page"

urlpatterns = [path("", views.index, name="index"),
                path("", views.about, name="about"),
                path("", views.movie, name="movie")
               ]
