from django.db import models
from django.contrib.auth.models import User
from .exercise_model import Exercise
from django.utils import timezone



class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="goals")
    target_weight = models.FloatField()
    target_reps = models.IntegerField()
    target_date = models.DateField(default=timezone.now)

    def __str__(self):
      return f"{self.user.username} - {self.exercise.name} ({self.exercise.abbreviation}): {self.target_weight} on {self.target_date}"

    
    