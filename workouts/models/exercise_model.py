from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10, default='--')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"





