from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogotypeListSerialiser
from .models import Logotype
# Create your views here.

class LogotypeListView(APIView):

    def get(self, request):
        logo = Logotype.objects.all()
        logo_serializer = LogotypeListSerialiser(logo, many=True).data
        return Response(logo_serializer)
       