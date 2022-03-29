from django.db import models

# Create your models here.

class Background(models.Model):
    backgrounds = models.FileField(upload_to='backgrounds/')
