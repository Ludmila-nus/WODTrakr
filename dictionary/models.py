from django.db import models

class Term(models.Model):
    category = models.CharField(max_length=50)
    term = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self):
        return self.term

