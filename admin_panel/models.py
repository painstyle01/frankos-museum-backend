from django.db import models
from django.db.models.fields import CharField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Card(models.Model):
    sub_title = CharField("Subtitle", max_length=50)
    title = CharField("Title", max_length=100)
    text = RichTextUploadingField(blank=True, null=True)
    time_event = CharField("Time of Event", max_length=100)
    details_information = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Article(models.Model):
    article = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.article
