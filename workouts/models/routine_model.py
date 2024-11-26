# Defines a CrossFit routine, which is a series of exercises to be performed in a specific format.
# The 'type' field categorizes the routine (e.g., AMRAP, EMOM, For Time), allowing users to structure their training sessions.
# A Routine may have multiple associated Workouts (individual exercises with details).

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routine')
    date = models.DateField(default=timezone.now, null=True, blank=True)
    type = models.CharField(
        max_length=20,
        choices=[
            ("for_time", "For Time"),
            ("amrap", "AMRAP"),
            ("emom", "EMOM"),
            ("rft", "Rounds for Time"),
            ("chipper", "Chipper"),
            ("endurance", "Endurance"),
            ("tabata", "Tabata"),
        ],
        default="for_time"
    )

    notes = RichTextField('Notes', blank=True, null=True)

    def __str__(self):
        return f"Routine for {self.user.username} on {self.date}"
    
    