from django.shortcuts import render, redirect
from django.http import JsonResponse
from recommendations.models import Movie
from django.db.models import Q, CharField, TextField
from django.middleware.csrf import get_token
import json


# Initial landing page view.
def index(request):
    return render(request, "landing_page/index.html")


def about(request):
    return render(request, "landing_page/about.html")


def contact(request):
    return render(request, "landing_page/contact.html")

def about(request):
    return render(request, "landing_page/about.html")

#testing purposes
def movie(request):
    return render(request, "landing_page/movie.html")

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrf_token": csrf_token})


def search_movies(request):
    query = request.GET.get("query")

    if query:
        # Get all field names of the Movie model
        movie_fields = [
            field.name
            for field in Movie._meta.get_fields()
            if isinstance(field, (CharField, TextField))
        ]

        # Construct a list of Q objects for each field
        q_objects = [Q(**{f"{field}__icontains": query}) for field in movie_fields]

        # Combine all Q objects using OR operator
        # movies = Movie.objects.filter(*q_objects).distinct()
        # json_movies = [{"movie": movie} for movie in movies]
        json_movies = [
            {"name": "spiderman", "year": 2023},
            {"name": "batman", "year": 1999},
        ]

        return render(request, "landing_page/movie.html", {"movies": json_movies})

    return redirect("")


def search_movies_json(request):
    if request.method == "POST":
        # Decode the request body
        body_unicode = request.body.decode("utf-8")

        # Parse the JSON data
        body_data = json.loads(body_unicode)

        # Access specific fields from the JSON data
        search_string = body_data.get("search")
        movies = [{"name": "Batman Begins"}]

        if search_string and False:  # And False until the DB works
            movies = Movie.objects.filter(name__icontains=search_string)

        # Perform search operation and get the result
        result = {"movies": movies}  # Your search result data here

        # Return the result as JSON response
        return JsonResponse(result, status=200)

    # Return an error response for non-POST requests
    return JsonResponse({"error": "Method not allowed"}, status=405)
