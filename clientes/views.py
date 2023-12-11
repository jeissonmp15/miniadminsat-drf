from rest_framework.response import Response
from clientes.models import Clientes
from rest_framework.views import APIView
from clientes.serializers import ClientesSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


class ClientesAPIView(APIView):
    model = Clientes

    def get(self, request, pk=None):
        if pk is not None:
            return self.detail(request, pk)
        queryset = self.model.objects.all()
        serializer =  ClientesSerializer(queryset, many=True)
        return Response(serializer.data)

    def detail(self, request, pk):
        queryset = self.model.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ClientesSerializer(instance)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.model.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = ClientesSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = self.model.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        nombre = instance.nombre
        instance.delete()
        return Response({'detail': f'El cliente {nombre} se a eliminado'})

