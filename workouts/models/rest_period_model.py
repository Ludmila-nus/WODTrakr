from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class RestPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restPeriod')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
      return f"Rest period from {self.start_date} to {self.end_date}"


