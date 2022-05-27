from django.db import models

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=55, verbose_name="Name of Ticket")
    text = models.TextField(default="The ticket doesn't have details at the moment")

    def __str__(self):
        return self.name



class Rule(models.Model):
    text = models.TextField(default="There're no rules at the moment")