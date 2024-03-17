from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def recommend_view(request):

    if request.method == "POST":
        answers = request.POST["answers"]
