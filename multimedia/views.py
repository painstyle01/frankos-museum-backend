from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CatalogyAudio, CatalogyVideo, Video, Audio, Image
from .serializers import (
    CatalogyVideoListSerializer,
    CatalogyAudioListSerializer,
    VideoListSerializer,
    AudioListSerializer,
    ImageListSerializer,
)

# Create your views here.


class CatalogyVideoListView(APIView):
    def get(self, request):
        cat_video = CatalogyVideo.objects.all()
        serializer = CatalogyVideoListSerializer(cat_video, many=True)
        return Response(serializer.data)


class CatalogyAudioListView(APIView):
    def get(self, request):
        cat_audio = CatalogyAudio.objects.all()
        serializer = CatalogyAudioListSerializer(cat_audio, many=True)
        return Response(serializer.data)


class VideoListView(APIView):
    def get(self, request, link):
        video = Video.objects.filter(link_video=link)
        serializer = VideoListSerializer(video, many=True)
        return Response(serializer.data)


class AudioListView(APIView):
    def get(self, request, link):
        audio = Audio.objects.filter(link_audio=link)
        serializer = AudioListSerializer(audio, many=True)
        return Response(serializer.data)


class ImageListView(APIView):
    def get(self, request):
        image = Image.objects.all()
        serializer = ImageListSerializer(image, many=True)
        return Response(serializer.data)
