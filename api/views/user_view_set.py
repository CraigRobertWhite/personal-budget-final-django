from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'head']

    def list(self, request, *args, **kwargs):
        raise PermissionDenied()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_object(self):
        if self.kwargs.get(self.lookup_url_kwarg or self.lookup_field) == 'current':
            self.kwargs[self.lookup_field] = self.request.user.id
        return super().get_object()
