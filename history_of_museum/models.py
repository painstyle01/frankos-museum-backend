from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class AboutMuseum(models.Model):
    article_m = RichTextUploadingField()

    def __str__(self):
        return self.article_m


class AboutFranko(models.Model):
    article_f = RichTextUploadingField()

    def __str__(self):
        return self.article_f
