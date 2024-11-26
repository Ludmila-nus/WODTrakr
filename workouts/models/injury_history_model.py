from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class InjuryHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='injuriHistory')
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
      return f"{self.user.username} - {self.description} on {self.date}"
    
