from django.shortcuts import render
from django.http import JsonResponse
from recommendations.models import Movie


# Initial landing page view.
def index(request):
    return render(request, "landing_page/index.html")


# Add other views here
def search_movies(request):
    query = request.GET.get("query")

    if query:
        movies = Movie.objects.filter(name__icontains=query)
        data = [{"name": movie.name, "year": movie.year} for movie in movies]
    else:
        data = {"name: null"}

    return JsonResponse(data, safe=False)
