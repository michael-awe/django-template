from django.urls import path
from . import views

app_name = "recommendations"

urlpatterns = [
    path("", views.index, name="index"),
    path("recommend/", views.recommend_view, name="recommend"),
]
