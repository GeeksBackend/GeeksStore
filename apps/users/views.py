from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer
from apps.users.permissions import UserPermission

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
    
    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return (UserPermission(), )
        return (AllowAny(), )