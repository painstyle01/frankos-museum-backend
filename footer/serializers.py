from rest_framework import serializers

from .models import Logotype

class LogotypeListSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Logotype
        fields = ('id', 'name_partners', 'link_partners', 'logotype')
    