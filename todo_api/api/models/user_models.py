from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

