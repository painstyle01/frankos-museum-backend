from rest_framework import serializers

from .models import CatalogyAudio, CatalogyVideo, Video,  Audio, Image

class CatalogyVideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatalogyVideo
        fields = '__all__'


class CatalogyAudioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatalogyAudio
        fields = '__all__'


class VideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class AudioListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = '__all__'


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
        