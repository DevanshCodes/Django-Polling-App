from django.shortcuts import render
from django.http import HttpResponse
from.models import Question

def index(random):
    questionLatestList = Question.objects.order_by('-publishedDate')[:5]
    context={
        'questionLatestList':questionLatestList,
    }
    return render(random,'Poll/index.html',context)

def pollmain(request):
    return HttpResponse("Hello This is the Polling Page")

def detail(random,question_id):
    question = Question.objects.get(pk=question_id)
    return render(random,'Poll/details.html',{'question':question})

def results(random,question_id):
    return HttpResponse("Your are looking at the results of Question %s."% question_id)    
def vote(random,question_id):
    return HttpResponse("Your are looking at votes of Question %s."% question_id)


# Create your views here.
