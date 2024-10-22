from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=50
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    comment = models.TextField(
        verbose_name='web comment'
    )
    created_at = models.DateTimeField(
        verbose_name='date and time created',
        default=timezone.now
    )
    contacted = models.BooleanField(
        verbose_name='¿have you contacted him?',
        default=False
    )

    def __str__(self):
        return self.name