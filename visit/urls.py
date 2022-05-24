from django.urls import path

from . import views

urlpatterns = [
    path('', views.TicketView.as_view()),
    path('<int:pk>', views.DetailsTicketView.as_view()),
]