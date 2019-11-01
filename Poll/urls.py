from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('poll/', views.pollmain, name='pollmain'),
    path('poll/<int:question_id>/',views.detail,name='Details'),
    path('poll/<int:question_id>/results',views.results,name='Results'),
    path('poll/<int:question_id>/votes',views.vote,name='votes'),
    
    
]