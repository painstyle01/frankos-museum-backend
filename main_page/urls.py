from django.urls import path

from . import views


urlpatterns = [
    path("", views.BackgroundListView.as_view(), name='home'),
]
