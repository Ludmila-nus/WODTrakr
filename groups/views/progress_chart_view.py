from django.http import JsonResponse
from django.views.generic import View
from workouts.models.workout_model import Workout
from django.contrib.auth.mixins import LoginRequiredMixin

class ProgressChartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Filter the authenticated user's workouts that are shared with the group
        user_workouts = Workout.objects.filter(user=request.user, shared_with_group=True)
        data = {
            'labels': [p.date for p in user_workouts],
            'weights': [p.weight for p in user_workouts],
            'exercises': [p.exercise for p in user_workouts],
        }
        return JsonResponse(data)
