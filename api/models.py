from django.db import models
from django.db.models.fields.files import ImageField

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


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    source_name = models.TextField(max_length=100)
    date = models.DateField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    author = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    picture = ImageField(upload_to="books/")

    def __str__(self):
        return str(self.id)


class ActualNews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300)
    author = models.TextField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=30)
    date = models.DateField()
