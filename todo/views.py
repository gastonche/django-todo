from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from datetime import datetime

from .models import Task
from .forms import ToDoForm
# Create your views here.


def index(request):
    all_task = Task.objects.order_by('-created_at')
    context = {'all_task': all_task}
    return render(request, 'todo/index.html', context)


def create(request):
    context = {}
    context['form'] = ToDoForm()
    return render(request, 'todo/create.html', context)


def save(request):
    form = ToDoForm(request.POST)
    task = form.save()
    task.created_at = datetime.today()
    task.updated_at = datetime.today()
    task.save()
    return redirect('/')


def detail(request, task_id):
    task_detail = get_object_or_404(Task, pk=task_id)
    form = ToDoForm(instance=task_detail)
    return render(request, 'todo/details.html', {'form':form, 'task': task_detail})


def update(request, task_id):
    task_detail = get_object_or_404(Task, pk=task_id)
    form = ToDoForm(request.POST, instance=task_detail)
    form.save()
    task_detail.updated_at = datetime.today()
    task_detail.save()
    return redirect('/'+str(task_id)+'/')
