from django.shortcuts import render

# Initial landing page view.
def index(request):
    return render(request, 'landing_page/index.html')
    return render(request, "landing_page/about.html")


#Add other views here