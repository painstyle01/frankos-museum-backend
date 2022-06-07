from django.db import models
from django.db.models.fields.files import ImageField

from embed_video.fields import EmbedVideoField

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
    text = models.TextField(default="Hellp")
    picture = ImageField(upload_to="timeline/")
    date = models.DateField()


class ActualNewsArchive(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300, default="None")
    author = models.TextField(max_length=50, default="None")
    text = models.TextField(default="None")
    date = models.DateField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class ListVideo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to="picture/")
    inner_picture = ImageField(upload_to="picture/inner_pucture", default="default.png")
    description = models.TextField(default="None")

    def __str__(self):
        return self.title


class ListAudio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to="picture/")
    inner_picture = ImageField(upload_to="picture/inner_pucture", default="default.png")
    description = models.TextField(default="None")

    def __str__(self):
        return self.title


class VideoDetail(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    video_file = models.FileField(upload_to="video/", blank=True)
    youtube_link = EmbedVideoField(null=True, blank=True)
    link_video = models.ForeignKey(ListVideo, on_delete=models.PROTECT, blank=True)
    description = models.TextField(default="None")


class AudioDetail(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    video_file = models.FileField(upload_to="video/", blank=True)
    youtube_link = EmbedVideoField(null=True, blank=True)
    link_audio = models.ForeignKey(ListAudio, on_delete=models.PROTECT, blank=True)
    description = models.TextField(default="None")


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    image_file = models.FileField(upload_to="image/")


class IntelligentProgram(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="programs/intelligent")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(ListVideo, on_delete=models.PROTECT)


class ArtProgram(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="programs/art")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(ListVideo, on_delete=models.PROTECT)


class EducationalProgram(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="programs/art")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(ListVideo, on_delete=models.PROTECT)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="projects/")
    title = models.CharField(max_length=155)
    subtitle = models.CharField(max_length=355)
    link = models.URLField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, verbose_name="Name of Ticket")
    text = models.TextField(default="The ticket doesn't have details at the moment")

    def __str__(self):
        return self.name


class Rule(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(default="There're no rules at the moment")


class Background(models.Model):
    id = models.AutoField(primary_key=True)
    backgrounds = models.FileField(upload_to="backgrounds/")


class Exposition(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="exposition/")
    title = models.CharField(max_length=155)
    subtitle = models.CharField(max_length=355)
    description = models.TextField(default="None")


class Collections(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="collections/")
    title = models.CharField(max_length=155)
    description = models.TextField(default="None")
