from rest_framework import serializers

from .models import Background

class BackgroundListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Background
        fields = ('id', 'backgrounds')
