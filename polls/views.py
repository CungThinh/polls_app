from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm


# Create your views here.

def home(request):
    context = {
        "questions": Question.objects.all()
    }
    return render(request, 'polls/home.html', context)


def vote(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        selected_choice = request.POST['question_choice']
        if selected_choice == "option1":
            question.option_one_count += 1
        elif selected_choice == "option2":
            question.option_two_count += 1
        elif selected_choice == "option3":
            question.option_three_count += 1
        else:
            return HttpResponse("Invalid choice")
        question.save()
        return redirect('results', question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/vote.html', context)


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'polls/create.html', context)
