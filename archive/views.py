from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView

from  .models import Archive
from .serializers import ArchiveSerializer
from api.models import BlogPost
# Create your views here.

class PostArchiveView(APIView):
    def get(self, request):
        queryset = Archive.objects.all()
        serializer = ArchiveSerializer(queryset, many=True)
        return Response(serializer.data)


def post(request):
    news = BlogPost.objects.all().values()
    for row in news:
        if row['archived'] == True:
            archive = Archive.objects.create(
                url = row['url'],
                source_name = row['source_name'],
                date = row['date'],
                archived = row['archived']
            )
    news = BlogPost.objects.filter(archived = True).delete()
    return redirect('/archive/')
        
