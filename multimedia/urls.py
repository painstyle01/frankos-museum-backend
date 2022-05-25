from django.urls import path

from . import views


urlpatterns = [
    path("video/", views.CatalogyVideoListView.as_view()),
    path("video/<int:link>", views.VideoListView.as_view()),
    path("audio/", views.CatalogyAudioListView.as_view()),
    path("audio/<int:link>", views.AudioListView.as_view()),
    path("image/", views.ImageListView.as_view()),
]
