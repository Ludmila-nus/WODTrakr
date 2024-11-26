from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label="User name")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    