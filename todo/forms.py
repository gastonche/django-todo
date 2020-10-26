from django import forms
from .models import Task, TaskPriority

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority']

