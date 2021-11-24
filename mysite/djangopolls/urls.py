from django.urls import path
from . import views

app_name = 'djangopolls'
urlpatterns = [
    path('', views.index, name='django-polls'),
    path('<int:question_id>/', views.detail, name='django-details'),
    path('<int:question_id>/results/', views.results, name='django-results'),
    path('<int:question_id>/vote/', views.vote, name='django-vote'),
]