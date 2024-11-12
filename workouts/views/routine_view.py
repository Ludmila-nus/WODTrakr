from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ..models.workout_model import Workout
from ..forms.workout_form import WorkoutForm
from ..forms.routine_form import RoutineForm
from ..forms.known_workout_form import KnownWorkoutForm


class RoutinesView(LoginRequiredMixin, TemplateView):
    template_name = "workouts/routines.html"


class CreateRoutineView(LoginRequiredMixin, TemplateView):
    template_name = "workouts/create_routine.html"
    success_url = reverse_lazy("routines")

    def form_valid(self, form):
        # Assign the logged in user to the field 'user'
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_form"] = (
            WorkoutForm()
        )  # an instance of the class (a form object to use and fill in the HTML) is created.
        context["routinet_form"] = RoutineForm()
        context["known_workout_form"] = KnownWorkoutForm()
        return context

    def post(self, request, *args, **kwargs):

        if "workout_form" in request.POST:
            form = WorkoutForm(request.POST)
        elif "routinet_form" in request.POST:
            form = RoutineForm(request.POST)
        elif "known_workout_form" in request.POST:
            form = KnownWorkoutForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            form.save()
            return redirect(self.success_url)

        return render(
            request,
            self.template_name,
            {
                "workout_form": WorkoutForm,
                "routinet_form": RoutineForm,
                "known_workout_form": KnownWorkoutForm,
                "form" : form, # is a shortcut to the submitted form, useful when you want to display specific validation errors
            },
        )


class ListRoutinesView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workouts/list_routines.html"
    context_object_name = "routines"

    def get_queryset(self):
        # Filter the routines to show only those of the authenticated user
        return Workout.objects.filter(user=self.request.user)
