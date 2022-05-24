from django.contrib import admin
from .models import Product, BlogPost


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
