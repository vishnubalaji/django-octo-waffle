from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all(),
        'title':'Django Home'
    }
    return render(request, 'polls/home.html', context)

def polls(request):
    return render(request, 'polls/polls.html', {'title':'Django Polls'})
