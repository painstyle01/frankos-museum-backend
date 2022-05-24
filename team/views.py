from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Department, Employee
from .serializers import DepartmentListSerializer, EmployeeListSerializer

# Create your views here.


class DepartmentListView(APIView):
    def get(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentListSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeListView(APIView):
    def get(self, request, pk):
        queryset = Employee.objects.filter(department_key=pk)
        serializer = EmployeeListSerializer(queryset, many=True)
        return Response(serializer.data)
