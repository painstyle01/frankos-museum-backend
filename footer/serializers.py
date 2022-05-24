from rest_framework import serializers

from .models import Logotype, SocialNetwork


class LogotypeListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Logotype
        fields = ("id", "name_partners", "link_partners", "logotype")


class SocialNetworkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = "__all__"
