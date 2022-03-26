from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    url_to_photo = models.TextField()
    avaliable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
