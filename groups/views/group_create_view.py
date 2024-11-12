from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..models.workout_group_model import WorkoutGroup
from django.contrib.auth.mixins import LoginRequiredMixin

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = WorkoutGroup
    fields = ['name', 'invite_code']
    template_name = 'groups/group_form.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
