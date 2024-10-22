from django.shortcuts import render
from ..models.user_preferences_model import UserPreferences
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin



@login_required
def user_preferences(request):
    return render(request, "users/user_preferences.html")

# LoginRequiredMixin