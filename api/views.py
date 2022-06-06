import random
from django.conf import settings
from .models import (
    Product, 
    BlogPost, 
    ActualNews, 
    Timeline, 
    Library, 
    ListAudio,
    ListVideo, 
    VideoDetail, 
    AudioDetail,
    Image,
    IntelligentProgram,
    ArtProgram,
    EducationalProgram,
    ActualNewsArchive,
    Project,
    Ticket,
    Rule,
    Background,
    Exposition,
    Collections
    )
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import (
    ProductSerializer,
    BlogPostSerializer,
    ActualNewsSerializer,
    LibrarySerializer,
    TimelineSerializer,
    ListAudioSerializer,
    ListVideoSerializer,
    VideoDetailSerializer,
    AudioDetailSerializer,
    ImageSerializer,
    IntelligentProgramSerializer,
    ArtProgramSerializer,
    EducationalProgramSerializer,
    ActualNewsArchiveSerializer,
    ProjectSerializer,
    TicketSerializer,
    RuleSerializer,
    BackgroundSerializer, ExpositionSerializer, CollectionsSerializer
)
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from liqpay import LiqPay
import json
from django.core.mail import send_mail

LIQPAY_PUBKEY = "sandbox_i34833063512"
LIQPAY_PRIVATE = "sandbox_cuqc4wGddoGwXZz0spEhMpkanF4NY88Ja8ADeUQo"


@csrf_exempt
def donate(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode())
        send_mail(
            subject="Нове замовлення",
            message=f"До вас пступило нове замовлення: {data.get('order')}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[data.get("to_email")],
        )
        return HttpResponse("300 Send")
    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        cash = data["money"]
        liqpay = LiqPay(LIQPAY_PUBKEY, LIQPAY_PRIVATE)
        html = liqpay.cnb_form(
            {
                "action": "pay",
                "amount": cash,
                "currency": "UAH",
                "description": "Donation",
                "order_id": random.randint(1, 19999999),
                "version": "3",
            }
        )
        return HttpResponse(html)
    else:
        return HttpResponse(404)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint to look/add/edit product for shops.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    Endpoint for adding,deleting news from main page.
    """

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    """
    Endpoint for adding,deleting news from main page.
    """

    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class TimelineViewSet(viewsets.ModelViewSet):
    """
    Endpoint for adding,deleting news from main page.
    """

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class ActualNewsViewSet(viewsets.ModelViewSet):
    """
    Endpoint for adding,deleting news from main page.
    """

    queryset = ActualNews.objects.all()
    serializer_class = ActualNewsSerializer


class ActualNewsArchiveViewSet(viewsets.ViewSet):
    def list(self, requset):
        news = ActualNews.objects.filter(archived=True).values()
        if news:
            for row in news:
                archive = ActualNewsArchive.objects.create(
                    title = row['title'],
                    author = row['author'],
                    text = row['text'],
                    date = row['date'],
                    archived = row['archived']
                )
        news = ActualNews.objects.filter(archived=True).delete()

        queryset = ActualNewsArchive.objects.all()
        serializer = ActualNewsArchiveSerializer(queryset, many=True)
        return Response(serializer.data)


class BackgroundViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Background.objects.last()
        serializer_class = BackgroundSerializer(queryset)
        return Response(serializer_class.data)


class ListVideoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ListVideo.objects.all()
        serializer_class = ListVideoSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self,request, pk=None):
        sety = VideoDetail.objects.filter(link_video=pk)
        serializer_class = VideoDetailSerializer(sety, many=True)
        return Response(serializer_class.data)


class ListAudioViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ListAudio.objects.all()
        serializer_class = ListAudioSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = AudioDetail.objects.filter(link_audio = pk)
        serializer_class = AudioDetailSerializer(queryset, many=True)
        return Response(serializer_class.data)


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class IntelligentProgramViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = IntelligentProgram.objects.all()
        serializer_class = IntelligentProgramSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset1 = ListVideo.objects.get(id = pk)
        queryset2 = VideoDetail.objects.filter(link_video = pk)
        serializer_class1 = ListVideoSerializer(queryset1)
        serializer_class2 = VideoDetailSerializer(queryset2, many=True)
        return Response(
            {
                "video": serializer_class1.data,
                "video_detail": serializer_class2.data
            }
        )

    
class ArtProgramViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ArtProgram.objects.all()
        serializer_class = ArtProgramSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset1 = ListVideo.objects.get(id = pk)
        queryset2 = VideoDetail.objects.filter(link_video = pk)
        serializer_class1 = ListVideoSerializer(queryset1)
        serializer_class2 = VideoDetailSerializer(queryset2, many=True)
        return Response(
            {
                "video": serializer_class1.data,
                "video_detail": serializer_class2.data
            }
        )


class EducationalProgramViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = EducationalProgram.objects.all()
        serializer_class = EducationalProgramSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def retrieve(self, request, pk=None):
        queryset1 = ListVideo.objects.get(id = pk)
        queryset2 = VideoDetail.objects.filter(link_video = pk)
        serializer_class1 = ListVideoSerializer(queryset1)
        serializer_class2 = VideoDetailSerializer(queryset2, many=True)
        return Response(
            {
                "video": serializer_class1.data,
                "video_detail": serializer_class2.data
            }
        )


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class RuleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Rule.objects.last()
        serializer_class = RuleSerializer(queryset)
        return Response(serializer_class.data)

class ExpositionViewSet(viewsets.ModelViewSet):
    queryset = Exposition.objects.all()
    serializer_class = ExpositionSerializer

class CollectionsViewSet(viewsets.ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer