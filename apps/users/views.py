from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.request.method == "POST")
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer