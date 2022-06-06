from .models import (
    Product,
    BlogPost,
    Library,
    Timeline,
    ActualNews,
    ListVideo,
    ListAudio,
    VideoDetail,
    AudioDetail,
    Image,
    IntelligentProgram,
    ArtProgram,
    EducationalProgram,
    ActualNewsArchive,
    Project,
    Ticket,
    Rule,
    Background, Exposition, Collections
)
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
        fields = ("id", "title", "date", "text", "picture")


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ("id", "name", "author", "description", "picture")


class ActualNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActualNews
        fields = ("id", "title", "author", "text", "date", "archived")


class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ("id", "backgrounds")


class ListVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListVideo
        fields = ("id", "title", "picture", "inner_picture", "description")


class ListAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAudio
        fields = ("id", "title", "picture", "inner_picture", "description")


class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetail
        fields = ("id", "title", "video_file", "youtube_link", "description", "link_video")


class AudioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioDetail
        fields = ("id", "title", "video_file", "youtube_link", "description", "link_audio")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "title", "image_file")


class IntelligentProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntelligentProgram
        fields = ("id", "image", "title", "subtitle", "link_detail")


class ArtProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtProgram
        fields = ("id", "image", "title", "subtitle", "link_detail")


class EducationalProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalProgram
        fields = ("id", "image", "title", "subtitle", "link_detail")


class ActualNewsArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActualNewsArchive
        fields = ("id", "title", "author", "text", "date")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "image", "title", "subtitle", "link")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "name", "text")


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ("id", "text")


class ExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposition
        fields = ("id", "image", "title", "subtitle", "description")


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ("id", "image", "title", "description")
