from django.db import models
from django.contrib.auth.models import User
from .exercise_model import Exercise
from django.utils import timezone
from ckeditor.fields import RichTextField


class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="goals", null=True, blank=True)
    target_weight = models.FloatField(null=True, blank=True)
    target_reps = models.IntegerField(null=True, blank=True)
    target_sets = models.IntegerField(null=True, blank=True)
    target_rounds = models.IntegerField(default=1, null=True, blank=True)
    target_time = models.DurationField(help_text="Duration in minutes:seconds", null=True, blank=True)
    target_date = models.DateField(default=timezone.now, null=True, blank=True)
    achieved_date = models.DateField(default=timezone.now, null=True, blank=True)
    notes = RichTextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
      status = "Completed" if self.is_completed else "Pending"
      return f"{self.user.username} - {self.exercise.name} ({self.exercise.abbreviation}): {self.target_weight} on {self.target_date} - {status}"

    
    