from django.shortcuts import render
from .forms import *
from .models import Recommendation

# TODO make this short and concise and move step-by-step (this is JUST for step 1 -> step 2 right now)
def recommend_view(request):
    form = GenreForm(request.POST)
    if form.is_valid():
        selected_genres = form.cleaned_data.get("Genres", [])
        # Recommendation(genres=selected_genres)
        # Recommendation.save()

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
