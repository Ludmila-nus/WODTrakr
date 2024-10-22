from django.urls import path
from .views.routine_view import CreateRoutineView
from .views.progress_view import progress
from .views.goals_view import set_goals, create_goals
from .views.additional_view import summary, compare_routines, log_rest, view_statistics
from .views.dashboard_view import DashboardView


app_name = "workouts"

urlpatterns = [
  
  path("create_routine/", CreateRoutineView.as_view, name="create_routine"),
  #path("list_routines/", list_routines, name="list_routines"),
  path("progress/", progress, name="progress"),
  path("create_goals/", create_goals, name="create_goals"),
  path("set_goals/", set_goals, name="set_goals"),
  path("view_statistics/", view_statistics, name="view_statistics"),
  path("summary/", summary, name="summary"),
  path("compare_routines/", compare_routines, name="compare_routines"),
  path("log_rest/", log_rest, name="log_rest"),
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
