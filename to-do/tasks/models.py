from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self) -> str:
        return self.title