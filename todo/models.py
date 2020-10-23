from django.db import models
from enum import Enum


class TaskPriority(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class TaskStatus(Enum):
    PENDING = 'pending'
    STARTED = 'starting'
    COMPLETED = 'completed'
    CANCELLED = 'Cancelled'


class Task(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    priority = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in TaskPriority],
        default=TaskPriority.LOW
    )
    status = models.CharField(
        max_length=40,
        choices=[(state, state.value) for state in TaskStatus],
        default=TaskStatus.PENDING
    )
    created_at = models.DateTimeField('Date Created')
    updated_at = models.DateTimeField('Last update')

    def __str__(self):
        return self.name

