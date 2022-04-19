from rest_framework import serializers

from .models import Department, Employee

class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class EmployeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'image', 'name', 'position', 'phone', 'department_key')
