from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProjectView.as_view(), name='project'),
]