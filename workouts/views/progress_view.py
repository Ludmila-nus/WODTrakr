from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def progress(request):
    return render(request, "workouts/progress.html") # View to show the maximum weights and repetitions achieved
