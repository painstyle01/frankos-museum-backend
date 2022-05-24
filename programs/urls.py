from django.urls import path

from . import views

urlpatterns = [
    path("intelligent", views.IntelligentProgramListView.as_view(), name="intelligent"),
    path("art", views.ArtProgramListView.as_view(), name="art"),
    path("educational", views.EducationalProgramListView.as_view(), name="educational"),
    path("<slug:slug_k>/", views.DetailView.as_view()),
]
