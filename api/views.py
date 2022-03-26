from .models import Product
from rest_framework import viewsets
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint to look/add/edit product for shops.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

