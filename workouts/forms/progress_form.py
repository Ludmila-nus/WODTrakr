from django import forms
from ..models.workout_model import Workout

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-control'}),
        }