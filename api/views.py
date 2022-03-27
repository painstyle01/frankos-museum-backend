import random

from .models import Product
from rest_framework import viewsets
from api.serializers import ProductSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from liqpay import LiqPay
import json


LIQPAY_PUBKEY = "sandbox_i34833063512"
LIQPAY_PRIVATE = "sandbox_cuqc4wGddoGwXZz0spEhMpkanF4NY88Ja8ADeUQo"

@csrf_exempt
def donate(request):
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
