from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ..models.workout_model import Workout
from ..forms.workout_form import WorkoutForm
from ..forms.routine_form import RoutineForm
from ..forms.known_workout_form import KnownWorkoutForm
from django.forms import modelformset_factory
from ..forms.workout_form import WorkoutFormSet
from django.http import JsonResponse
from django.template.loader import render_to_string


class RoutinesView(LoginRequiredMixin, TemplateView):
    template_name = "workouts/routines.html"

class ListRoutinesView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workouts/list_routines.html"
    context_object_name = "routines"

    def get_queryset(self):
        # Filter the routines to show only those of the authenticated user
        return Workout.objects.filter(user=self.request.user)


class CreateRoutineView(LoginRequiredMixin, FormView):
    template_name = "workouts/create_routine.html"
    success_url = reverse_lazy("workouts:routines")
    form_class = RoutineForm

    def form_valid(self, form):
        # Assign the logged-in user to the routine
        form.instance.user = self.request.user
        routine = form.save()

        # Handle AJAX requests specifically
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            workout_formset = WorkoutFormSet(self.request.POST)
            if workout_formset.is_valid():
                # Save each workout and link it to the routine
                workouts = workout_formset.save(commit=False)
                for workout in workouts:
                    workout.routine = routine
                    workout.user = self.request.user
                    workout.save()

                # Render the updated FormSet HTML to send back to the client
                formset_html = render_to_string(
                    "workouts/workout_formset.html",
                    {"workout_formset": WorkoutFormSet(queryset=Workout.objects.filter(routine=routine))},
                    request=self.request,
                )
                return JsonResponse({"success": True, "routine_id": routine.id, "formset_html": formset_html})
            else:
                # Return errors if the FormSet is invalid
                return JsonResponse({"success": False, "errors": workout_formset.errors})

        # For standard requests, proceed with the default behavior
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # Detect which form is being submitted
        if "known_workout_form" in request.POST:
            form = KnownWorkoutForm(request.POST)
            if form.is_valid():
                # Save the known workout with the logged-in user
                known_workout = form.save(commit=False)
                known_workout.user = request.user
                known_workout.save()
                return JsonResponse({"success": True, "message": "Known workout saved!"})
            return JsonResponse({"success": False, "errors": form.errors})

        elif "routine_form" in request.POST:
            # Delegate routine form handling to FormView's default `post` method
            return super().post(request, *args, **kwargs)

        elif "workout_formset" in request.POST:
            workout_formset = WorkoutFormSet(request.POST)
            if workout_formset.is_valid():
                # Save workouts in the FormSet
                workout_formset.save()
                return JsonResponse({"success": True, "message": "Workouts saved!"})
            return JsonResponse({"success": False, "errors": workout_formset.errors})

        # Handle invalid or unexpected form submissions
        return JsonResponse({"success": False, "message": "Invalid form submission."})
