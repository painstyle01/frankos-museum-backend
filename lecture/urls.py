import django

from django.urls import path

from . import views


urlpatterns = [path("post/", views.LectureView.as_view(), name="lucture")]
