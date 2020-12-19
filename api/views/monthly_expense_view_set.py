from rest_framework.viewsets import ModelViewSet

from api.models import MonthlyExpense
from api.serializers import MonthlyExpenseSerializer


class MonthlyExpenseViewSet(ModelViewSet):
    queryset = MonthlyExpense.objects.all()
    serializer_class = MonthlyExpenseSerializer
    http_method_names = ['get', 'patch', 'head', 'post']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
