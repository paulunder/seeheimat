from django.shortcuts import render
from .models import Service

def home(request):
    return render(request, 'pages/home.html')

# def services(request):
#     return render(request, 'pages/services.html')

def services_view(request):
    services = Service.objects.all()
    return render(request, 'pages/services.html', {'services': services})
