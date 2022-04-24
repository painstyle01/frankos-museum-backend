from email.mime import base
from django.urls import path, re_path
from rest_framework import routers

from .views import DepartmentListView, EmployeeListView

# route = routers.DefaultRouter()
# route.register(r'team', DepartmentListViewSet, basename='department')
# route.register(r'team/{employee}', EmployeeListViewSet, basename='employee')


urlpatterns = [
    path('team/', DepartmentListView.as_view()),
    path('team/<int:pk>', EmployeeListView.as_view()),
]