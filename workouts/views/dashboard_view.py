from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Exercise, Workout, Goals, InjuryHistory, RestPeriod
from django.db.models import Avg


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/dashboard.html'  # Template to render

    def get_context_data(self, **kwargs):
        # Call the original context
        context = super().get_context_data(**kwargs)
        
        # Get recent exercises
        context['recent_exercises'] = Exercise.objects.filter(user=self.request.user).order_by('-date')[:5]
        
        # Get recent workouts
        context['recent_workouts'] = Workout.objects.filter(user=self.request.user).order_by('-date')[:5]

        # Get goals
        context['goals'] = Goals.objects.filter(user=self.request.user)
        
        # Get injury history
        context['injury_history'] = InjuryHistory.objects.filter(user=self.request.user)
        
        # Get rest periods
        context['rest_periods'] = RestPeriod.objects.filter(user=self.request.user)
        
        # Calculate average duration of workouts
        average_duration = (
            context['recent_workouts'].aggregate(Avg('time'))['time__avg']
            if context['recent_workouts'].exists() else 0
        )
        context['average_workout_duration'] = average_duration

        return context
