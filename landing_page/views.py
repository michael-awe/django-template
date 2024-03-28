from django.shortcuts import render


# Initial landing page view.
def index(request):
    return render(request, "landing_page/movie.html")


# Add other views here
