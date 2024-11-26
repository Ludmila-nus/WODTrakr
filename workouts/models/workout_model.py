# Links a Routine to specific exercises and provides details about the workout, such as weight, reps, and sets.
# This model allows each routine to have multiple exercises with unique attributes, allowing tracking of each exercise's progression.
# The 'shared_with_group' flag indicates whether the workout is shared with a workout group.

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from .exercise_model import Exercise
from .routine_model import Routine
from django.contrib.auth.models import User
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
    date = models.DateField(default=timezone.now, null=True, blank=True)
    notes = RichTextField(blank=True, null=True)
    group = models.ForeignKey(
        WorkoutGroup,
        on_delete=models.SET_NULL,
        related_name="workouts",
        null=True,
        blank=True,
    )
    shared_with_group = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        #  Checks if there is a routine and if the routine has a user associated with it.
        routine_user = {self.routine.user.username} if self.routine and self.routine.user else "No Routine"
        # Check if there is an associated exercise
        exercise_name = self.exercise.name if self.exercise else "No Exercise"
        return f"{routine_user} - {exercise_name} ({self.exercise.abbreviation if self.exercise else ''}): {self.weight} on {self.date}"

   
   
