from rest_framework import serializers

from .models import Ticket, Rule


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"
        

class RuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rule
        fields = "__all__"
