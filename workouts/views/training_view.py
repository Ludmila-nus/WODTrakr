from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ..models.workout_model import Workout
from ..forms.workout_form import WorkoutForm, WorkoutFormSet
from ..forms.routine_form import RoutineForm
from ..forms.known_workout_form import KnownWorkoutForm
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.middleware.csrf import get_token



class TrainingManagerView(LoginRequiredMixin, TemplateView):
    template_name = "workouts/training_manager.html"

class ListTrainingView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workouts/list_training.html"
    context_object_name = "routines"

    def get_queryset(self):
        # Filter the routines to show only those of the authenticated user
        return Workout.objects.filter(user=self.request.user)


class CreateGenericFormView(LoginRequiredMixin, FormView):
    form_class = WorkoutForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save()
        response_data = {"success": True, "message": f"{self.model_name} created!"}
        
        if self.model_name == 'Routine':
            # Generate the FormSet related to the routine
            formset = WorkoutFormSet(queryset=Workout.objects.filter(routine=instance) or Workout.objects.none())

            # Render FormSet to HTML
            formset_html = render_to_string("workouts/formset.html", {
                "formset": formset,
                "csrf_token": get_token(self.request),
            })                    

            response_data['routine_id'] = instance.id 
            response_data['formset_html'] = formset_html
        
        return JsonResponse(response_data)

    def form_invalid(self, form):
        return JsonResponse({"success": False, "errors": form.errors}, status=400)

# TrainingView inherits from this base class and reuses its logic, dynamically assigning the model_name 
# and handling multiple forms using a form_type attribute in the POST
class TrainingView(CreateGenericFormView):
    template_name = "workouts/training.html"
    form_class = WorkoutForm
    success_url = reverse_lazy("workouts:training_manager")

    # Add forms to the context for rendering in the template 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout_form"] = WorkoutForm()  # Empty form
        context["routine_form"] = RoutineForm()  # Empty form
        context["known_workout_form"] = KnownWorkoutForm()  # Empty form
        context["workout_formset"] = WorkoutFormSet()  # Empty FormSet 
        return context
    
    # Handle POST requests for different form types
    def post(self, request, *args, **kwargs):
        form_type = request.POST.get('form_type')

        if form_type == 'workout':
            form = WorkoutForm(request.POST)
            self.model_name = "Workout"
            return self.form_valid(form) if form.is_valid() else self.form_invalid(form)

        elif form_type == 'routine':
            form = RoutineForm(request.POST)
            self.model_name = "Routine"
            return self.form_valid(form) if form.is_valid() else self.form_invalid(form)
        
        elif form_type == 'KnownWorkout':
            form = KnownWorkoutForm(request.POST)
            self.model_name = "KnownWorkout"
            return self.form_valid(form) if form.is_valid() else self.form_invalid(form) 

        elif form_type == 'workout_formset':
            formset = WorkoutFormSet(request.POST)
            self.model_name = "Workout"
            
            if formset.is_valid():
                # Process and save each form in the FormSet
                for workout in formset.save(commit=False):
                    workout.user = request.user # Associate the workout with the logged-in user
                    workout.save() # Save the workout instance
                
                return JsonResponse({"success": True, "message": "Workouts saved!"})
            else:
                # Return errors if the FormSet validation fails
                return JsonResponse({"success": False, "errors": formset.errors})


        return JsonResponse({"success": False, "message": "Invalid form type"}, status=400)
    