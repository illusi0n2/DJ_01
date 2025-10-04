from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home_task/index.html')

def about(request):
    return render(request, 'home_task/about.html')

def services(request):
    return render(request, 'home_task/services.html')

def contact(request):
    return render(request, 'home_task/contact.html')