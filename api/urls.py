from django.urls import path

from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('', views.send_email_with_order, name='email')
]