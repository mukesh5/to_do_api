from django.db import models

from api.models.user_models import User


class Task(models.Model):
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
