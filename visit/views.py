from rest_framework.views import  APIView
from rest_framework.response import Response

from .serializers import TicketSerializer, DetailsTicketSerializer
from .models import Ticket, DetailsTicket
# Create your views here.


class TicketView(APIView):

    def get(self, requset):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)


class DetailsTicketView(APIView):

    def get(self, requset, pk):
        queryset = DetailsTicket.objects.filter(ticket_key = pk)
        serializer = DetailsTicketSerializer(queryset, many=True)
        return Response(serializer.data)
        