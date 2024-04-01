from django.shortcuts import render, redirect
from django.http import JsonResponse
from recommendations.models import Movie


# Initial landing page view.
def index(request):
    return render(request, "landing_page/index.html")


def show_movies(request):
    return render(request, "landing_page/movie.html")


# Add other views here
def search_movies(request):
    query = request.GET.get("query")

    if query:
        # movies = Movie.objects.filter(name__icontains=query)
        # json_movies = [{"name": movie.name, "year": movie.year} for movie in movies]
        json_movies = [
            {"name": "spiderman", "year": 2023},
            {"name": "batman", "year": 1999},
        ]

        return render(request, "landing_page/movie.html", {"movies": json_movies})

    return redirect("")
