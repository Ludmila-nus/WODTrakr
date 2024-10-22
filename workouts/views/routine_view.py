from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from ..models.workout_model import Workout
from ..forms.workout_form import WorkoutForm

class CreateRoutineView(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workouts/create_routine.html'
    success_url = reverse_lazy('dashboard')  # Redirige a la página de dashboard después de guardar

    def form_valid(self, form):
        # Asignar el usuario logueado al campo 'user'
        form.instance.user = self.request.user
        return super().form_valid(form)


#def create_routine(request):
#
#    return render(request, "workouts/create_routine.html") # View for the user to add a new workout routine, including notes 
#
#def list_routines(request):
#    return render(request, "workouts/list_routines.html") # View to display all of the user's workout routines
#
#
#def create_workout(request):
#    if request.method == "POST":
#        form = WorkoutForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('workouts:list_routines')
#    else:
#        form = WorkoutForm()
#
#    context = {
#        'form': form
#    }    
#
#    return render(request, "workouts/create_routine.html", context)
#