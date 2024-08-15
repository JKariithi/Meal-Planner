from django.db import models

# Create your models here.

class Days(models.Model):
    """The Day of the week"""
    day = models.CharField(max_length=50)


    def __str__(self):
        """A representation of the model"""
        return self.day

