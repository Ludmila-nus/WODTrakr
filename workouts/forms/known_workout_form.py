from django import forms
from ..models.known_workout_model import KnownWorkout

class KnownWorkoutForm(forms.ModelForm):
    class Meta:
        model = KnownWorkout
        exclude = ['user']
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            'name': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

 