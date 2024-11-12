from django.db import models
from django.conf import settings
from workouts.models.routine_model import Routine

class WorkoutGroup(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_groups')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='workout_group')
    invite_code = models.CharField(max_length=10, unique=True)
    routine_of_the_day = models.ForeignKey('workouts.Routine', on_delete=models.SET_NULL, null=True, blank=True, related_name='daily_group_routine')

    def __str__(self):
        return self.name