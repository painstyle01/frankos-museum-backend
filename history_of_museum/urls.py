from django.urls import path

from . import views

urlpatterns = [
    path("about-dimfranka/", views.AboutMuseumView.as_view(), name="dimfranka"),
    path("about-franko/", views.AboutFrankoView.as_view(), name="franko"),
]
