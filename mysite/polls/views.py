from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
        'name':'Vishnu Balaji',
        'age':21
    },
    {
        'name':'PyTorcher',
        'age':23
    }
]

def home(request):
    context = {
        'posts':posts,
        'title':'Django Home'
    }
    return render(request, 'polls/home.html', context)

def polls(request):
    return render(request, 'polls/polls.html', {'title':'Django Polls'})
