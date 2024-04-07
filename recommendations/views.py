from django.shortcuts import render
from .forms import *
from .models import Recommendation


def recommend_view(request):
    form = YearForm()
    return render(
        request,
        "recommendations/index.html",
        {"form": form},
    )


def index(request):
    form = GenreForm()
    return render(
        request,
        "recommendations/index.html",
        {"form": form},
    )
