from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Background
from .serializers import BackgroundListSerializer
# Create your views here.

class BackgroundListView(APIView):
    """class of background"""
    def get(self, request):
        latest_id = Background.objects.latest('id').id
        backgrounds = Background.objects.filter(id = latest_id)
        bg_serializer = BackgroundListSerializer(backgrounds, many = True).data
        return Response(bg_serializer)
