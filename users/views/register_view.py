from django.views import View
from django.shortcuts import render, redirect
from ..forms.userRegister_form import UserRegisterForm
from django.contrib.auth.models import User

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password2 = form.cleaned_data['password2']
            user = User.objects.create_user(username=username, email=email, password=password2)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            context = {
                'msj': 'Usuario creado correctamente'
            }
            return render(request, "workouts/dashboard.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "users/register.html", context)



