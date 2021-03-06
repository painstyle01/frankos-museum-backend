from rest_framework import serializers

from .models import Excursion


class ExcursionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields = ("id", "excursion", "text")
