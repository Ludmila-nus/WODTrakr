from django.views.generic.edit import UpdateView
from ..models.user_profile_model import UserProfile
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormView


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = "users/profile_detail.html"
    context_object_name = "profile" # in the template I will have a profile variable, where I can reference all the fields of the profile 

    def get_initial(self):
        self.initial['profile_pk'] =  self.get_object().pk
        return super().get_initial()

    def get_success_url(self):
        return reverse('profile_detail', args=[self.get_object().pk])    


class ProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "users/profile_update.html"
    context_object_name = "profile"
    fields = ['profile_picture', 'full_name', 'birthdate']

    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object() # Gets the current profile
        if user_profile.user != self.request.user: # Checks if the profile belongs to the authenticated user
            return HttpResponseRedirect(reverse(''))
        return super().dispatch(request, *args, **kwargs) # Continues with normal flow
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Perfil editado correctamente.")
        return super(ProfileUpdateView, self).form_valid(form)
        
    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])
    

# Note:
# - self.get_object(): Used to explicitly retrieve the object related to the view.
#   Common in views like DetailView or DeleteView, and respects any custom logic 
#   defined in the get_object() method.
# - self.object: A direct reference to the object being processed by the view.
#   Available after the form is successfully saved (in form_valid or later),
#   typically used in views like CreateView and UpdateView.
















