from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from .exercise_model import Exercise
from .routine_model import Routine
from django.contrib.auth.models import User
from django.utils import timezone


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout")
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name="workout")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="workout")
    weight = models.FloatField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    rounds = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.routine.user.username} - {self.exercise.name} ({self.exercise.abbreviation}): {self.weight} on {self.date}"
    