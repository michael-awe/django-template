from django.shortcuts import render, redirect


def recommend_view(request):
    print(request)


def index(request):
    return render(request, "recommendations/index.html")
