from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    profile_picture = models.ImageField('Profile image', upload_to='profile_pictures/', blank=True, null=True)
    full_name = models.CharField('Full name', max_length=150, blank=True, null=True)
    birthdate = models.DateField('Birthdate', blank=True, null=True)
    created_at = models.DateTimeField('Created at', default=now)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.user.username

