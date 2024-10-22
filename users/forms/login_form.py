from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    