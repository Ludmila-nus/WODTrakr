# Represents individual exercises in CrossFit (e.g., Squat, Deadlift) with unique names and abbreviations.
# This model serves as a reference for exercises that can be included in workout routines.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="exercises")
    name = models.CharField(max_length=100, null=True, blank=True)
    abbreviation = models.CharField(max_length=10, default='--', null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True,)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"





