from django import forms
from ..models.routine_model import Routine

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        exclude = ['user']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

