from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View

from users.forms.login_form import LoginForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    
    def form_valid(self, form):
        # We extract the data from the form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # We authenticate the user
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            # If the user is valid, we log in
            login(self.request, user)
            return redirect(reverse('workouts:dashboard'))
        else:
            # If the user is invalid, we resend with an error
            return self.form_invalid(form, error_message="Invalid user")
    
    def form_invalid(self, form, error_message=None):
        # Handle the invalid form and display the error message
        context = self.get_context_data(form=form, error=True, error_message=error_message)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        # To pass error_message to the context if it exists
        context = super().get_context_data(**kwargs)
        context['error'] = kwargs.get('error', False)
        context['error_message'] = kwargs.get('error_message', None)
        return context
    
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('core:welcome'))

