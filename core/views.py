from rest_framework import viewsets

from core.models import Product, ProductItem, ProductItemTransition
from core.serializers import ProductSerializer, ProductItemTransitionSerializer, ProductItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.select_related("item").all()
    serializer_class = ProductItemSerializer


class ProductItemTransitionViewSet(viewsets.ModelViewSet):
    queryset = ProductItemTransition.objects.select_related("product_item").all()
    serializer_class = ProductItemTransitionSerializer

# Create your views here.
