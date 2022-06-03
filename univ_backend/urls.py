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
router.register(r"news", views.NewsViewSet)
router.register(r"timeline", views.TimelineViewSet)
router.register(r"actualnews", views.ActualNewsViewSet)
router.register(r'library', views.LibraryViewSet)
router.register(r"background", views.BackgroundViewSet, basename="background")
router.register(r"list-video", views.ListVideoViewSet, basename="video")
router.register(r"list-audio", views.ListAudioViewSet, basename="audio")
router.register(r"image", views.ImageViewSet)
router.register(r"program-intelligent", views.IntelligentProgramViewSet, basename="intelligent")
router.register(r"program-art", views.ArtProgramViewSet, basename="art")
router.register(r"program-educational", views.EducationalProgramViewSet, basename="educational")
router.register(r"archive", views.ActualNewsArchiveViewSet, basename="archive")
router.register(r"project", views.ProjectViewSet)
router.register(r"ticket", views.TicketViewSet)
router.register(r"rule", views.RuleViewSet, basename='rule')
urlpatterns = [
    path("footer/", include("footer.urls")),
    path("contacts/", include("contacts.urls")),
    path("", include("team.urls")),
    path("", include("excursions.urls")),
    path("", include("history_of_museum.urls")),
    path("lecture/", include("lecture.urls")),
    re_path(r"^api/donate", include("api.urls")),
    re_path(r"^api/", include(router.urls)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
