from django.shortcuts import render
from django.Https import HttpResponse


def home(request):
    return HttpResponse("Hello World")
# Create your views here.
