from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import CatalogyAudio, CatalogyVideo, Video, Audio, Image

# Register your models here.


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


class CatalogyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(CatalogyVideo, CatalogyAdmin)
admin.site.register(CatalogyAudio, CatalogyAdmin)

admin.site.register(Video, VideoAdmin)
admin.site.register(Audio)
admin.site.register(Image)
