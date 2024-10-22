from django import forms
from django.contrib.auth.password_validation import validate_password


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=140, label="User name")
    first_name = forms.CharField(max_length=140, label="Name")
    last_name = forms.CharField(max_length=140, label="Last name")
    email = forms.EmailField(max_length=140, label="Email")

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat your password', widget=forms.PasswordInput)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2 and password1 != '':
            raise forms.ValidationError('Passwords do not match')

        if password2 != '':
            validate_password(password2)

        return password2
    