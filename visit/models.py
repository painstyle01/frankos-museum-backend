from django.db import models

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=55, verbose_name="Name of Ticket")

    def __str__(self):
        return self.name


class DetailsTicket(models.Model):
    text = models.TextField()
    ticket_key = models.ForeignKey(Ticket, verbose_name='which ticket', on_delete=models.PROTECT)