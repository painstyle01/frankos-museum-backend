from django.db import models
from django.db.models.fields.files import ImageField

from embed_video.fields import EmbedVideoField
# Create your models here.

class CatalogyVideo(models.Model):
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to='picture/')
    inner_picture = ImageField(upload_to = 'picture/inner_pucture')
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title


class  CatalogyAudio(models.Model):
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to='picture/')
    inner_picture = ImageField(upload_to = 'picture/inner_pucture')
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250)
    video_file = models.FileField(upload_to='video/',blank=True)
    youtube_link = EmbedVideoField(null=True,blank=True)
    slug_catalogy_video = models.ForeignKey(CatalogyVideo, to_field='slug', on_delete=models.PROTECT)
    description = models.TextField()


class Audio(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio/')
    slug_catalogy_audio = models.ForeignKey(CatalogyAudio, to_field='slug', on_delete=models.PROTECT)
    description = models.TextField()


class Image(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image_file = models.FileField(upload_to='image/')
