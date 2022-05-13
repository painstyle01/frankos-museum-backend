from django.urls import path

from . import views

urlpatterns = [
    path('', views.get, name='archive'),
    path('<int:id>', views.post_save)
]