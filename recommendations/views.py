from django.shortcuts import render
from .forms import GenreForm


def recommend_view(request):
    print(request)


def index(request):
    form = GenreForm()
    return render(
        request,
        "recommendations/index.html",
        {"form": form},
    )
