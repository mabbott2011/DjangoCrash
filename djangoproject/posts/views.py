from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #link = "https://www.youtube.com/watch?v=D6esTdOLXh4"
    return HttpResponse('Hello from POSTS!')
