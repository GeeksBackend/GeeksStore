from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.carts.models import Cart, CartItem
from apps.carts.serializers import CartSerializer, CartItemSerializer

# Create your views here.
class CartAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemAPI(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer