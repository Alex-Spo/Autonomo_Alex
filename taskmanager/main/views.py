from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main', 'tasks': tasks})

def questions(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/questions.html', {'title': 'Questions-Answers', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html', {'title': 'Paiment'})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def program(request):
    return render(request, 'main/program.html', {'title': 'Program'})


