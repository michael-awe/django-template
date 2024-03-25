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
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    data = [{"name": movie.name, "year": movie.year} for movie in movies]
    return JsonResponse(data, safe=False)
