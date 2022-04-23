from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Excursion
from .serializers import ExcursionListSerializer
# Create your views here.

class ExcursionListView(APIView):

    def get(self, request):
        queryset = Excursion.objects.all()
        serializer = ExcursionListSerializer(queryset, many=True)
        return Response({'excursion': serializer.data})

