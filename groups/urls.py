from django.urls import path
from .views.group_create_view import GroupCreateView
from .views.group_list_view import GroupListView
from .views.progress_chart_view import ProgressChartView

app_name = 'groups'

urlpatterns = [
    path('create/', GroupCreateView.as_view(), name='create'),
    path('list/', GroupListView.as_view(), name='list'),
    path('progress-chart/', ProgressChartView.as_view(), name='progress_chart'),
]
