from django.urls import path
from .views.routine_view import RoutinesView, CreateRoutineView, ListRoutinesView
from .views.progress_view import ProgressView, ProgressTemplateView
from .views.goals_view import set_goals, create_goals
from .views.additional_view import summary, compare_routines, log_rest, view_statistics
from .views.dashboard_view import DashboardView


app_name = "workouts"

urlpatterns = [
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  path('routines/', RoutinesView.as_view(), name='routines'),
  path("create_routine/", CreateRoutineView.as_view(), name="create_routine"),
  path("list_routines/", ListRoutinesView.as_view(), name="list_routines"),
  path('progress/', ProgressTemplateView.as_view(), name='progress'),  # Displays the HTML template
  path('progress_data/', ProgressView.as_view(), name='progress_data'),  # Provides the JSON
  path("create_goals/", create_goals, name="create_goals"),
  path("set_goals/", set_goals, name="set_goals"),
  path("view_statistics/", view_statistics, name="view_statistics"),
  path("summary/", summary, name="summary"),
  path("compare_routines/", compare_routines, name="compare_routines"),
  path("log_rest/", log_rest, name="log_rest"),
]
