from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from.models import Question, Choices
from  django.urls import reverse

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
    question = Question.objects.get(pk=question_id)
    return render (random, 'Poll/results.html', {'question':question})
    return HttpResponse("Your are looking at the results of Question %s."% question_id)    
def vote(random,question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=random.POST["choice"])
    except  (KeyError,Choices.DoesNotExist):
        return render(random, 'Poll/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Results', args=(question.id,)))


# Create your views here.
