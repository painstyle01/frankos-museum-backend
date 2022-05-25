from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    IntelligentProgramListSerializer,
    ArtProgramListSerializer,
    EducationalProgramListSerializer,
)
from .models import IntelligentProgram, ArtProgram, EducationalProgram

from multimedia.models import CatalogyVideo, Video
from multimedia.serializers import CatalogyVideoListSerializer, VideoListSerializer

# Create your views here.


class IntelligentProgramListView(APIView):
    def get(self, request):
        queryset = IntelligentProgram.objects.all()
        serializer = IntelligentProgramListSerializer(queryset, many=True)
        return Response(serializer.data)


class ArtProgramListView(APIView):
    def get(self, request):
        queryset = ArtProgram.objects.all()
        serializer = ArtProgramListSerializer(queryset, many=True)
        return Response(serializer.data)


class EducationalProgramListView(APIView):
    def get(self, request):
        queryset = EducationalProgram.objects.all()
        serializer = EducationalProgramListSerializer(queryset, many=True)
        return Response(serializer.data)


class DetailView(APIView):
    def get(self, request, link):
        queryset_catalog_video = get_object_or_404(CatalogyVideo, id=link)
        queryset_video = Video.objects.filter(link_video=link)
        serializer_cat_video = CatalogyVideoListSerializer(queryset_catalog_video)
        serializer_video = VideoListSerializer(queryset_video, many=True)
        return Response(
            {
                "detail_catalog_video": serializer_cat_video.data,
                "detail_video": serializer_video.data,
            }
        )
