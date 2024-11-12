from django import forms
from ..models.known_workout_model import KnownWorkout

class KnownWorkoutForm(forms.ModelForm):
    class Meta:
        model = KnownWorkout
        exclude = ['user']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

