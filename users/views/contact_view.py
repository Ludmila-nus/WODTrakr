from ..forms.contact_form import ContactForm
from django.core.mail import send_mail
from ..models.contact_model import Contact
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = "users/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        comment = form.cleaned_data["comment"] # Uso .get() para evitar KeyError
        
        message_content = f"{name} with email: {email} has wrote the below comment: {comment}"
                  

        Contact.objects.create(
            name=name, 
            email=email, 
            comment=comment)
        
        success = send_mail(
            "Subject here",
            message_content,
            "ludmilanussio@gmail.com",
            ["ludmilanussio@hotmail.com"],
            fail_silently=False,
        )
        
        
        return super().form_valid(form)
    
    
