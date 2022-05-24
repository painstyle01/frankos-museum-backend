import random
from django.conf import settings
from .models import Product, BlogPost, ActualNews, Timeline, Library
from rest_framework import viewsets
from api.serializers import (
    ProductSerializer,
    BlogPostSerializer,
    ActualNewsSerializer,
    LibrarySerializer,
    TimelineSerializer,
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
