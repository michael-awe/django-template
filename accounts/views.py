from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    return HttpResponse('logout babbyyy')

def register_view(request):
    return render(request, 'accounts/register.html')
