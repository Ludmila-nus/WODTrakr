from ..form import GoalsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView
from ..forms.goals_form import GoalsForm
from django.urls import reverse_lazy
from ..models import Goals
from django.http import JsonResponse
import json
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404 
from django.views.generic import ListView


class GoalsView(LoginRequiredMixin, TemplateView):
    template_name = "workouts/goals.html"

    def get_context_data(self, **kwargs):
        # Call the original context
        context = super().get_context_data(**kwargs)
        # puts the user's goals into context
        context["goals"] = Goals.objects.filter(user=self.request.user)
        return context


class GoalsSetView(LoginRequiredMixin, FormView):
    template_name = "workouts/set_goals.html"
    form_class = GoalsForm
    success_url = reverse_lazy("workouts:goals")

    def form_valid(self, form):
        goal = form.save(commit=False)
        goal.user = self.request.user
        # Save the form if valid
        goal.save()
        # Answer with a success message in JSON format
        return JsonResponse(
            {
                "success": True,
                "message": "Goal saved successfully!",
                "goal_id": goal.id,  # objet ID recently created
            }
        )

    def form_invalid(self, form):
        # Answer with errors in JSON format if the form is not valid
        return JsonResponse(
            {
                "success": False,
                "errors": form.errors,  # Django form errors
            },
            status=400,
        )

class GoalsListView(LoginRequiredMixin, ListView):
    model = Goals
    template_name = "workouts/goals_list.html" 
    context_object_name = "goals"  

    def get_queryset(self):
        return Goals.objects.filter(user=self.request.user)
    

class GoalsCheckView(LoginRequiredMixin, UpdateView):
    template_name = "workouts/check_goals.html"
    model = Goals
    fields = ['is_completed', 'achieved_date']
    success_url = reverse_lazy("workouts:goals_list")

    def get_context_data(self, **kwargs):
        # Call the original context
        context = super().get_context_data(**kwargs)
        # puts the user's goals into context
        context["goals"] = Goals.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):

        goal = get_object_or_404(Goals, pk=self.kwargs['pk'], user=request.user) # Get the goal object
        
        try:
            data = json.loads(request.body)

            is_completed = data.get("is_completed") == True
            achieved_date = data.get("achieved_date")

            goal.is_completed = is_completed
            goal.achieved_date = achieved_date if is_completed else None

            goal.save()

            return JsonResponse(
                {"success": True, "message": "Goal updated successfully!"}
            )
        except Goals.DoesNotExist:
                return JsonResponse(
                    {"success": False, "message": "Goal not found."}, status=404
                )
    
       
       
    
       
    