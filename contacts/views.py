from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ContactListSerializer
from .models import Contact

# Create your views here.


class ContactListView(APIView):
    def get(self, request):
        contact = Contact.objects.last()
        serializer = ContactListSerializer(contact)
        return Response({"contact": serializer.data})
