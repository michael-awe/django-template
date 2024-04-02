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

def about(request):
    return render(request, "landing_page/about.html")