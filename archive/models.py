from django.db import models

# Create your models here.
from api.models import ActualNews


class ActualNewsArchive(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300)
    author = models.TextField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

class Archive(ActualNewsArchive):
    pass
