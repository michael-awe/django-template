from django.shortcuts import render

# Initial landing page view.
def index(request):
    return render(request, 'landing_page/index.html')


#Add other views here