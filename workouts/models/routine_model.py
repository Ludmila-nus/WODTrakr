from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone


class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routine')
    date = models.DateField(default=timezone.now)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Routine for {self.user.username} on {self.date}"
    
    