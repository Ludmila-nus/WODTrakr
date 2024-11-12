# This model represents a catalog of well-known CrossFit workouts, often used globally with standard names and formats.
# Each KnownWorkout includes a name, description, and type, which categorizes the workout format (e.g., AMRAP, For Time).
# This model is useful for providing users with a pre-defined selection of structured workouts, reducing the need for manual input.
# It can be referenced by other models or views to streamline workout selection and provide consistent workout definitions.

from django.db import models

class KnownWorkout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
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
    )

    def __str__(self):
        return self.name
