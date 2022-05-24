from django.urls import path

from . import views

urlpatterns = [
    path("", views.LogotypeListView.as_view()),
    path("social-network", views.SocialNetworkListView.as_view()),
]
