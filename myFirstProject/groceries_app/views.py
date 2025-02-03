from django.shortcuts import render
from django.http import HttpResponse

def app_homepage(request):
    return HttpResponse("This is the newly created app")