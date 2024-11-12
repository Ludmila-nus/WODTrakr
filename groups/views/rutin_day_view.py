from django.views.generic.edit import UpdateView
from ..models.workout_group_model import WorkoutGroup

class SetRoutineOfTheDayView(UpdateView):
    model = WorkoutGroup
    fields = ['routine_of_the_day']  # The administrator selects the routine
    template_name = 'groups/set_routine_of_the_day.html'
    
    def get_queryset(self):
        # Ensure that only the group admin can modify the routine
        return self.request.user.admin_groups.all()
    
    def form_valid(self, form):
        # Saving the day's routine
        return super().form_valid(form)
