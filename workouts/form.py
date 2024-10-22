from django import forms
from .models import Workout, Goals

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise', 'weight', 'reps', 'sets', 'date', 'notes']
        widgets = {
            'exercise': forms.Select(),
        }

class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['exercise','target_weight', 'target_reps', 'target_date']
        widgets = {
            'exercise': forms.Select(),
        }        