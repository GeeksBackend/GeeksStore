from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

# Create your views here.
class ProductAPI(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrive(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer