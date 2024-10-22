from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    dark_mode = models.BooleanField('Dark mode', default=False)
    notifications_enabled = models.BooleanField('Notifications enabled', default=True)
    language = models.CharField('Language', max_length=10, choices=[('en', 'English'), ('es', 'Spanish')], default='en')
    time_zone = models.CharField('Time zone', max_length=50, default='UTC')

    def __str__(self):
        return f"Preferences for {self.user.username}"
