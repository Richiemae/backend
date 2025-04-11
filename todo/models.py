from django.db import models
from django.apps import AppConfig

class TodoConfig(AppConfig):
    name = 'todo'

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
