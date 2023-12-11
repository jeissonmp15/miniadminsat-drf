from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from activos.models import Activos
from activos.serializers import ActivosSerializer


class ActivosListAPIView(ListCreateAPIView):
    model = Activos
    serializer_class = ActivosSerializer

    def get_queryset(self):
        return self.model.objects.all()


class ActivosDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Activos
    serializer_class = ActivosSerializer

    def get_queryset(self):
        return self.model.objects.all()