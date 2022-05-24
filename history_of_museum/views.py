from django.http import HttpResponse
from django import views

from .models import AboutMuseum, AboutFranko

# Create your views here.


class AboutMuseumView(views.View):
    def get(self, request):
        data = AboutMuseum.objects.last()
        return HttpResponse(f"<div>{data}</div>")


class AboutFrankoView(views.View):
    def get(self, request):
        data = AboutFranko.objects.last()
        return HttpResponse(f"<div>{data}</div>")
