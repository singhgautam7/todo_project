from django.db import models
from django.utils import timezone
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    description = models.TextField(default="No description here")
    due_date = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["due_date"]     #adding hyphen just before due would order it in descending order

    def __str__(self):
        return self.title

    @property
    def is_expired(self):
        today=datetime.now
        return self.due_date<today
