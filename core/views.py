from django.views.generic import TemplateView
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'core/welcome.html'  

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('workouts:dashboard')  # To pass error_message to the context if it exists
        return super().get(request, *args, **kwargs)  # Display the welcome page if not authenticated

