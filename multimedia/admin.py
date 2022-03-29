from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import CatalogyAudio, CatalogyVideo, Video, Audio, Image
# Register your models here.

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(CatalogyVideo)
admin.site.register(CatalogyAudio)

admin.site.register(Video, VideoAdmin)
admin.site.register(Audio)
admin.site.register(Image)