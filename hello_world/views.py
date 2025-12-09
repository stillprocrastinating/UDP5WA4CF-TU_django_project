from django.shortcuts import render

from django.http import HttpResponse

# VIEWS

def index(request):
    return HttpResponse("Hello, world!")
