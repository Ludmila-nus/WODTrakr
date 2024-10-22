from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name")
    email = forms.EmailField(label="email")
    comment = forms.CharField(max_length=1000, label="comment", widget=forms.Textarea)
    
    def clean_name(self):
        
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            raise forms.ValidationError("Name's length must be more than 5 characters")
        return name
        
        
        