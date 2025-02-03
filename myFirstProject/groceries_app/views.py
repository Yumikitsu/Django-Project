from django.shortcuts import render
from django.http import HttpResponse

def app_homepage(request):
    return render(request, 'homepage.html')

def about_us(request):
    return render(request, "aboutUs.html")

def services(request):
    return render(request, "services.html")

def contact_us(request):
    return render(request, "contactUs.html")