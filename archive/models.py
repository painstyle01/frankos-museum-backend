from django.db import models

# Create your models here.


class ActualNewsArchive(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300,default='None')
    author = models.TextField(max_length=50,default='None')
    text = models.TextField(default='None')
    date = models.DateField()
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

class Archive(ActualNewsArchive):
    pass
