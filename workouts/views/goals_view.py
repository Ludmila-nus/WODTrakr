from django.shortcuts import render, redirect
from ..form import GoalsForm
from django.contrib.auth.decorators import login_required


@login_required
def set_goals(request):
    return render(request, "workouts/set_goals.html") # View for the user to set and edit their workout goals

@login_required
def create_goals(request):
    if request.method == "POST":
        form = GoalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts/summary.html')
    else:
        form = GoalsForm()

    context = {
        'form': form
    }    

    return render(request, "workouts/set_goals.html", context)
