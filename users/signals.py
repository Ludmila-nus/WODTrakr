from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models.user_profile_model import UserProfile

# Django does not automatically load the signals.py file, so it is necessary to import it in the ready() method of the apps.py file of the application.

class UserProfileSignals:
    @staticmethod
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Creates a UserProfile when a new User is created.
        """
        if created:
            UserProfile.objects.create(user=instance)

    @staticmethod
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Saves the UserProfile when the User is updated.
        """
        if hasattr(instance, 'profile'):
            instance.profile.save()
