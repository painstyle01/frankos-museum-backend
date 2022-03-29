from django.db import models
from django.db.models.fields.files import ImageField

from embed_video.fields import EmbedVideoField
# Create your models here.

class CatalogyVideo(models.Model):
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to='picture/')

    def __str__(self):
        return self.title


class  CatalogyAudio(models.Model):
    title = models.CharField(max_length=200)
    picture = ImageField(upload_to='picture/')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250)
    video_file = models.FileField(upload_to='video/',blank=True)
    youtube_link = EmbedVideoField(null=True,blank=True)
    link_video = models.ForeignKey(CatalogyVideo, on_delete=models.PROTECT)


class Audio(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio/')
    link_audio = models.ForeignKey(CatalogyAudio, on_delete=models.PROTECT)


class Image(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    image_file = models.FileField(upload_to='image/')
