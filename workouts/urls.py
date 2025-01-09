from django.urls import path
from .views.training_view import TrainingManagerView, ListTrainingView, TrainingView
from .views.progress_view import ProgressView, ProgressTemplateView
from .views.goals_view import GoalsView, GoalsSetView, GoalsCheckView, GoalsListView
from .views.additional_view import summary, compare_routines, log_rest, view_statistics
from .views.dashboard_view import DashboardView


app_name = "workouts"

urlpatterns = [
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  path('routines/', TrainingManagerView.as_view(), name='training_manager'),
  path("list_routines/", ListTrainingView.as_view(), name="list_training"),
  path("create_routine/", TrainingView.as_view(), name="training"),
  path('progress/', ProgressTemplateView.as_view(), name='progress'),  # Displays the HTML template
  path('progress_data/', ProgressView.as_view(), name='progress_data'),  # Provides the JSON
  path("goals/", GoalsView.as_view(), name="goals"),
  path("set_goals/", GoalsSetView.as_view(), name="set_goals"),
  path("goals_list/", GoalsListView.as_view(), name="goals_list"),
  path("check_goals<int:pk>/", GoalsCheckView.as_view(), name="check_goals"),
  path("view_statistics/", view_statistics, name="view_statistics"),
  path("summary/", summary, name="summary"),
  path("compare_routines/", compare_routines, name="compare_routines"),
  path("log_rest/", log_rest, name="log_rest"),
]

