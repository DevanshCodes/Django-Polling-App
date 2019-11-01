from django.urls import path
from . import views

urlpatterns = [
    path('', views.pollmain, name='pollmain'),
    path('<int:question_id>/',views.detail,name='Details'),
    path('<int:question_id>/results',views.results,name='Results'),
    path('<int:question_id>/votes',views.vote,name='votes'),
    
    
]