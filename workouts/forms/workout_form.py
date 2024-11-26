from django import forms
from ..models.workout_model import Workout
from django.forms import modelformset_factory


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ["user"]
        widgets = {
            "exercise": forms.Select(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "reps": forms.NumberInput(attrs={"class": "form-control"}),
            "sets": forms.NumberInput(attrs={"class": "form-control"}),
            "rounds": forms.NumberInput(attrs={"class": "form-control"}),
            "time": forms.TimeInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "shared_with_group": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


# Allows to handle multiple forms based on WorkoutForm
WorkoutFormSet = modelformset_factory(
    Workout,  # Base model
    form = WorkoutForm, # Form associated with each instance
    exclude = ["user"],
    fields=[
        "exercise",
        "weight",
        "reps",
        "sets",
        "rounds",
        "time",
        "date",
        "notes",
        "shared_with_group",
    ],
    extra=1, #Extra additional forms
)
