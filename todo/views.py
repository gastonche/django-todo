from django.shortcuts import render
#from django.http import HttpResponse

from .models import Task

# Create your views here.


def index(request):
    all_task = Task.objects.order_by('-created_at')
    context = {'all_task': all_task}

    return render(request, 'todo/index.html', context)
