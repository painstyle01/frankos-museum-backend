from rest_framework import serializers

from .models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "time", "location", "contact_us", "arrival")
