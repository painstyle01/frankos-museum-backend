from .models import Product, BlogPost
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "type", "name", "description", "price", "url_to_photo", "avaliable")


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "url", "source_name", "date")
