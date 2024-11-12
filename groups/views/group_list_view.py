from django.views.generic import ListView
from ..models.workout_group_model import WorkoutGroup
from django.contrib.auth.mixins import LoginRequiredMixin

class GroupListView(LoginRequiredMixin, ListView):
    model = WorkoutGroup
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return self.request.user.groups.all()
