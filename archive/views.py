from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Archive
from .serializers import ArchiveSerializer
from api.models import ActualNews

# Create your views here.


class ArchiveView(APIView):
    def get(self, request):
        news = ActualNews.objects.all().values()
        for row in news:
            if row["archived"] == True:
                archive = Archive.objects.create(
                    title = row['title'],
                    author = row['author'],
                    text = row['text'],
                    date = row['date'],
                    archived = row['archived']
            )
        news = ActualNews.objects.filter(archived=True).delete()

        queryset = Archive.objects.all()
        serializer = ArchiveSerializer(queryset, many=True)
        return Response(serializer.data)

