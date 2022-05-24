from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.FileField(upload_to='projects/')
    title = models.CharField(max_length=155)
    subtitle = models.CharField(max_length=355)
    link = models.URLField()

    def __str__(self):
        return self.title