from django import forms
from ..models.goals_model import Goals

class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        exclude = ["user"]
        widgets = {
            "exercise": forms.Select(attrs={"class": "form-control"}),
            "target_weight": forms.NumberInput(attrs={"class": "form-control"}),
            "target_reps": forms.NumberInput(attrs={"class": "form-control"}),
            "target_sets": forms.NumberInput(attrs={"class": "form-control"}),
            "target_rounds": forms.NumberInput(attrs={"class": "form-control"}),
            "target_time": forms.TimeInput(attrs={"class": "form-control"}),
            "target_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }