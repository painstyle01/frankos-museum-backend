from django.urls import path

from .views import ExcursionListView


urlpatterns = [
    path("excursion/", ExcursionListView.as_view(), name="excursion"),
]
