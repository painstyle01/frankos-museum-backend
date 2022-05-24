from rest_framework import serializers

from .models import Ticket, DetailsTicket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"


class DetailsTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailsTicket
        exclude = ['ticket_key']
        