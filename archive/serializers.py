from rest_framework import serializers

from .models import PostArchive

class ArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostArchive
        fields = "__all__"
