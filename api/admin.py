from django.contrib import admin
from .models import (
    ActualNews,
    Product, 
    BlogPost, 
    ListAudio, 
    ListVideo, 
    VideoDetail, 
    AudioDetail,
    IntelligentProgram,
    ArtProgram,
    EducationalProgram,
    ActualNewsArchive,
    Project, 
    Ticket,
    Rule,
    Background
    )


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "name", "description", "price", "avaliable")


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "source_name", "date")


class TimelineAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date")


class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "description", "picture")


class ActualNewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "text", "date", "archived")


admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(ActualNews,ActualNewsAdmin)
admin.site.register(Background)
admin.site.register(ListAudio)
admin.site.register(ListVideo)
admin.site.register(VideoDetail)
admin.site.register(AudioDetail)
admin.site.register(IntelligentProgram)
admin.site.register(ArtProgram)
admin.site.register(EducationalProgram)
admin.site.register(ActualNewsArchive)
admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(Rule)
