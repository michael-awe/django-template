from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from recommendations.models import Movie


# Create your views here.
def is_admin(user):
    return user.is_superuser


def index(request):

    # if user is not logged in, redirect to home page
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    return render(request, "dashboard/index.html")


def get_all_movies(request):
    all_movies = Movie.objects.all()

    return render(request, "dashboard/movies_list.html", {"movies": all_movies})


def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except:
        # Movie id doesn't exist
        return render(request, "dashboard/404.html")

    return render(request, "dashboard/movie_details.html", {"movie": movie})


@user_passes_test(is_admin)
def create_movie(request, movie_id):
    return render(request, "dashboard/404.html")


@user_passes_test(is_admin)
def delete_movie(request, movie_id):
    try:
        # movie = get_object_or_404(Movie, pk=movie_id)
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully"})
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)


@user_passes_test(is_admin)
def update_movie(request, movie_id):
    return render(request, "dashboard/404.html")
