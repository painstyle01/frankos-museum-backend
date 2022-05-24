from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArchiveView.as_view(), name="archive"),
]
