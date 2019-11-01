from django.shortcuts import render
from django.http import HttpResponse

def pollmain(request):
    return HttpResponse("Hello This is the Polling Page")

def detail(random,question_id):
    return HttpResponse("Your are looking at Question %s."% question_id)

def results(random,question_id):
    return HttpResponse("Your are looking at the results of Question %s."% question_id)    
def vote(random,question_id):
    return HttpResponse("Your are looking at votes of Question %s."% question_id)


# Create your views here.
