from rest_framework.viewsets import ModelViewSet
from equipos.models import Equipo
from equipos.serializers import EquiposSerializer, EquiposSelectSerializer, EquiposDetailSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class EquiposViewset(ModelViewSet):
    serializer_class = EquiposSerializer
    queryset = Equipo.objects.select_related('activo')


    @action(methods=['GET'], detail=False, serializer_class=EquiposSelectSerializer)
    def select(self, request):
        return self.list(request)


    @action(methods=['GET'], detail=True, serializer_class=EquiposDetailSerializer)
    def details(self, request, **kwargs):
        return self.retrieve(request)


    

