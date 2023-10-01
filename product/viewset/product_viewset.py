from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication # novo
from rest_framework.permissions import IsAuthenticated # novo

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication] # novo
    permission_classes = [IsAuthenticated] # novo
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')