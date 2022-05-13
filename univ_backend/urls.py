"""univ_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r"products", views.ProductViewSet)
router.register(r'news', views.NewsViewSet)
urlpatterns = [
    path('footer/', include("footer.urls")),
    path('contacts/', include('contacts.urls')),
    path('', include("main_page.urls")),
    path('', include("multimedia.urls")),
    path('', include("team.urls")),
    path('', include("excursions.urls")),
    path('', include("history_of_museum.urls")),
    path('events/', include('archive.urls')),
    re_path(r"^api/donate", include("api.urls")),
    re_path(r"^api/", include(router.urls)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^ckeditor/", include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
