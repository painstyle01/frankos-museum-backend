from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostArchiveView.as_view(), name="archive"),
    path("post/", views.post),
]
