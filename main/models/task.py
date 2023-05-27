from django.db import models

from .tag import Tag
from .user import User


class Task(models.Model):
    class State(models.TextChoices):
        NEW = "new task"
        IN_DEVELOPMENT = "in development"
        IN_QA = "in qa"
        IN_CODE_REVIEW = "in code review"
        READY_FOR_RELEASE = "ready for release"
        RELEASED = "released"
        ARCHIVED = "archived"

    class Priority(models.IntegerChoices):
        LOW = 0
        MEDIUM = 1
        HIGH = 2
        CRITICAL = 3

    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    date_finish = models.DateTimeField()
    state = models.CharField(
        max_length=255, default=State.NEW, choices=State.choices
    )
    priority = models.IntegerField(
        default=Priority.LOW, choices=Priority.choices
    )
    tags = models.ManyToManyField(Tag, related_name="tasks")
    task_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_tasks"
    )
    task_performer = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_tasks"
    )
