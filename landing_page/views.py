from django.shortcuts import render
from django.http import JsonResponse
from recommendations.models import Movie


# Initial landing page view.
def index(request):
    return render(request, "landing_page/index.html")


def about(request):
    return render(request, "landing_page/about.html")


def contact(request):
    return render(request, "landing_page/contact.html")


# Add other views here
#copyed and pasted missing material
def search_movies(request):
    query = request.GET.get("query")

    if query:
        movies = Movie.objects.filter(name__icontains=query)
        data = [{"name": movie.name, "year": movie.year} for movie in movies]
    else:
        data = {"name: null"}

    return JsonResponse(data, safe=False)

def about(request):
    return render(request, "landing_page/about.html")

#testing purposes
def movie(request):
    return render(request, "landing_page/movie.html")