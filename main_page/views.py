from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Background
from .serializers import BackgroundListSerializer

# Create your views here.


class BackgroundListView(APIView):
    """class of background"""

    def get(self, request):
        backgrounds = Background.objects.last()
        bg_serializer = BackgroundListSerializer(backgrounds).data
        return Response(bg_serializer)
