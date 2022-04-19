from django.contrib import admin
from .models import Product, BlogPost


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "name", "description", "price", "avaliable")


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "source_name", "date")


admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
