from django.urls import path

from . import views

urlpatterns = [
    path('', views.LogotypeListView.as_view())
]