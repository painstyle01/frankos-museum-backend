from rest_framework import serializers

from .models import IntelligentProgram, ArtProgram, EducationalProgram


class IntelligentProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntelligentProgram
        fields = '__all__'


class ArtProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtProgram
        fields = '__all__'

class EducationalProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalProgram
        fields = '__all__'