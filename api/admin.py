from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "type","name", "description", "price", "avaliable")


admin.site.register(Product, ProductAdmin)