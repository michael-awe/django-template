from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:index')
        else:
            #checks if username is taken
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'dashboard/signup.html', {
                    'form': form,
                    'message': 'Username has already been taken'
                })
            #checks if email is taken
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                return render(request, 'dashboard/signup.html', {
                    'form': form,
                    'message': 'Email address is already in use'
                })
            password1 = request.POST['password1']
            confirm = request.POST['password2']
            if password1 != confirm:
                return render(request, 'dashboard/signup.html', {
                    'form': form,
                    'message': 'Passwords do not match'
                })

            return render(request, 'dashboard/signup.html', {
                'form': form,
                'message': 'An unknown error occured.'
                })
    elif request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
