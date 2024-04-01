from django.shortcuts import render


# Initial landing page view.
def index(request):
    return render(request, "landing_page/index.html")


# Add other views here
def movie(request):
    return render(request, "landing_page/movie.html")

def about(request):
    return render(request, "landing_page/about.html")