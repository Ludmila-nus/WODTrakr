from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_statistics(request):
    return render(request, "workouts/view_statistics.html") # View to display detailed graphs and statistics

@login_required
def summary(request):
    return render(request, "workouts/summary.html") # View to generate and display workout summaries on a weekly or monthly basis

@login_required
def compare_routines(request):
    return render(request, "workouts/compare_routines.html") # View to compare different workout routines of the user

@login_required
def log_rest(request):
    return render(request, "workouts/log_rest.html") # View for the user to log a rest period
