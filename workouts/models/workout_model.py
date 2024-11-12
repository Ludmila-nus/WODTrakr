# Links a Routine to specific exercises and provides details about the workout, such as weight, reps, and sets.
# This model allows each routine to have multiple exercises with unique attributes, allowing tracking of each exercise's progression.
# The 'shared_with_group' flag indicates whether the workout is shared with a workout group.

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from .exercise_model import Exercise
from .routine_model import Routine
from django.contrib.auth.models import User
from django.utils import timezone
from groups.models.workout_group_model import WorkoutGroup


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout")
    routine = models.ForeignKey(
        Routine, on_delete=models.CASCADE, related_name="workout", null=True, blank=True
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="workout"
    )
    weight = models.FloatField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    sets = models.IntegerField(null=True, blank=True)
    rounds = models.IntegerField(default=1, null=True, blank=True)
    time = models.DurationField(help_text="Duration in minutes:seconds", null=True, blank=True)
    date = models.DateField(default=timezone.now)
    notes = RichTextField(blank=True, null=True)
    group = models.ForeignKey(
        WorkoutGroup,
        on_delete=models.SET_NULL,
        related_name="workouts",
        null=True,
        blank=True,
    )
    shared_with_group = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.routine.user.username} - {self.exercise.name} ({self.exercise.abbreviation}): {self.weight} on {self.date}"
