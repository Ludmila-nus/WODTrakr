from django import forms
from ..models.workout_model import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'rounds': forms.NumberInput(attrs={'class': 'form-control'}),
        }
