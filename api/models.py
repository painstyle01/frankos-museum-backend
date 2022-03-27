from django.db import models

PRODUCT_TYPE = (("book", "Книжка"), ("statue", "Фігурка"), ("trinket", "Брелок"))

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=300)
    type = models.CharField(choices=PRODUCT_TYPE, default="book", max_length=25)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    url_to_photo = models.TextField()
    avaliable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
