from django.db import models


from multimedia.models import CatalogyVideo

# Create your models here.


class IntelligentProgram(models.Model):
    image = models.ImageField(upload_to="programs/intelligent")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(
        CatalogyVideo, on_delete=models.PROTECT
    )


class ArtProgram(models.Model):
    image = models.ImageField(upload_to="programs/art")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(
        CatalogyVideo, on_delete=models.PROTECT
    )


class EducationalProgram(models.Model):
    image = models.ImageField(upload_to="programs/art")
    title = models.CharField(max_length=55, default="Франко вдома")
    subtitle = models.CharField(max_length=255, default="Блог")
    link_detail = models.ForeignKey(
        CatalogyVideo, on_delete=models.PROTECT
    )
