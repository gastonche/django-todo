from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse

from .models import Task, TaskPriority, TaskStatus

# Create your views here.


def index(request):
    all_task = Task.objects.order_by('-created_at')
    context = {'all_task': all_task}

    return render(request, 'todo/index.html', context)


def detail(request, task_id):
    task_detail = get_object_or_404(Task, pk=task_id)
    statuses = TaskStatus.choices;
    priorities = TaskPriority.choices;
    return render(request, 'todo/details.html', {'task': task_detail, 'statuses': statuses, 'priorities': priorities})

def update(request, task_id):
    pass
