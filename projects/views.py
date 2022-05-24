from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project
# Create your views here.


class ProjectView(APIView):

    def get(self,request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
        