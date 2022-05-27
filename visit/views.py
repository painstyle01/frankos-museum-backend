from rest_framework.views import  APIView
from rest_framework.response import Response

from .serializers import TicketSerializer, RuleSerializer
from .models import Ticket, Rule
# Create your views here.


class TicketView(APIView):

    def get(self, requset):
        queryset = Ticket.objects.all()
        serializer_ticket = TicketSerializer(queryset, many=True)
        return Response(serializer_ticket.data )


class RulesView(APIView):
    def get(self, requset):
        queryset = Rule.objects.last()
        serializer = RuleSerializer(queryset)
        return Response(serializer.data)
