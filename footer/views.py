from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LogotypeListSerialiser, SocialNetworkListSerializer
from .models import Logotype, SocialNetwork

# Create your views here.


class LogotypeListView(APIView):
    def get(self, request):
        logo = Logotype.objects.all()
        logo_serializer = LogotypeListSerialiser(logo, many=True).data
        return Response(logo_serializer)


class SocialNetworkListView(APIView):
    def get(self, request):
        social_network = SocialNetwork.objects.all()
        serializer = SocialNetworkListSerializer(social_network, many=True).data
        return Response(serializer)
