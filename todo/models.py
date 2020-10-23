from django.db import models
#from enum import Enum


class TaskPriority(models.TextChoices):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class TaskStatus(models.TextChoices):
    PENDING = 'pending'
    STARTED = 'starting'
    COMPLETED = 'completed'
    CANCELLED = 'Cancelled'


class Task(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    priority = models.CharField(
        max_length=20,
        choices=TaskPriority.choices,
        default=TaskPriority.LOW
    )
    status = models.CharField(
        max_length=40,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )
    created_at = models.DateTimeField('Date Created')
    updated_at = models.DateTimeField('Last update')

    def __str__(self):
        return self.name

