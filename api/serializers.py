from .models import Product, BlogPost, Library, Timeline, ActualNews
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "type",
            "name",
            "description",
            "price",
            "url_to_photo",
            "avaliable",
        )


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "url", "source_name", "date")


class TimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields = ("id", "title", "date")


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ("id", "name", "author", "description", "picture")


class ActualNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActualNews
        fields = ("id", "title", "author", "text", "date", "archived")
