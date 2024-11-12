from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from workouts.models.workout_model import Workout
from collections import defaultdict


class ProgressView(LoginRequiredMixin, View):
        
    def get(self, request, *args, **kwargs):

        user_workouts = Workout.objects.filter(user=request.user).order_by('exercise', 'date')

        progress_data = defaultdict(list)

        exercise_name = None

        for workout in user_workouts:
            exercise_name = workout.exercise.name
            if progress_data[exercise_name]:
                last_entry = progress_data[exercise_name][-1]
                weight_increase = workout.weight - last_entry['weight']

            else:   
                weight_increase = 0

            progress_data[exercise_name].append({
                   'date': workout.date,
                   'weight': workout.weight,
                   'weight_increase': weight_increase
                })        
        
        data = {
            'exercises': [
                {
                    'exercise': exercise,
                    'history': progress_data[exercise]
                }
                for exercise in progress_data
            ]
        }


        return JsonResponse(data)


class ProgressTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/progress.html'  # Template to render
