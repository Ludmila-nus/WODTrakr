from django import forms
from ..models.routine_model import Routine

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


