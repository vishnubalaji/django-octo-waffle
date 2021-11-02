from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='polls-home'),
    path('polls/', views.polls, name='polls-polls'),
]