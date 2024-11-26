from django.views.generic.edit import CreateView
from ..forms.userRegister_form import UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterView(CreateView):
    template_name = "users/register.html"
    model = User
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "user successfully created")
        return super(RegisterView, self).form_valid(form)
































