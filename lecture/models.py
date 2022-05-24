from django.db import models

# Create your models here.


class Lecture(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=55)
    comment = models.TextField()

    def __str__(self):
        return self.name
