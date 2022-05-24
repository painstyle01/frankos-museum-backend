from django.db import models

# Create your models here.


class Excursion(models.Model):

    excursion = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.excursion
