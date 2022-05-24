from django.db import models

# Create your models here.


class Contact(models.Model):
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact_us = models.CharField(max_length=300)
    arrival = models.CharField(max_length=400)

    def __str__(self):
        return self.time
