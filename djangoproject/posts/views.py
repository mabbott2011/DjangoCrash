from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


# Create your views here.

def index(request):
    #link = "https://www.youtube.com/watch?v=D6esTdOLXh4"
    #return HttpResponse('Hello from POSTS!')

    #Pull the first 10 Post objects
    posts = Posts.objects.all()[:10]

    data = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', data)

def details(request, id):
    post = Posts.objects.get(id=id)

    data = {
        'post': post
    }

    return render(request, 'posts/details.html', data)
