from django.db import models

# Create your models here.

class Logotype(models.Model):

    name_partners = models.CharField(max_length=100)
    link_partners = models.URLField(max_length=200, null=True)
    logotype = models.FileField(upload_to='logotype/')


class SocialNetwork(models.Model):

    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    logo = models.FileField(upload_to='social_network/')
    