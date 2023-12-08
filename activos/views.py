from django.shortcuts import render, get_object_or_404

from activos.models import Activos
from clientes.models import Clientes

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ActivosAPIView(APIView):
    model = Activos
    permission_classes = [AllowAny]

    def get(self, request, pk):
        return Response({'datos': True})



def get(request):
    queryset = Activos.objects.all()
    context = {'lista': queryset}
    return render(request, 'activos/activos.html', context)


def retrieve(request, pk):
    activo = get_object_or_404(Activos, pk=pk)
    return render(request, 'activos/activo-detalle.html', {'instancia': activo})


def update(request, pk):
    activo = get_object_or_404(Activos, pk=pk)
    if request.method == 'POST':
        activo.nombre = request.POST['nombre']
        activo.placa = request.POST.get('placa', None)
        activo.tipo_activo = request.POST['tipo_activo']
        activo.cliente_id = request.POST['cliente_id']

        activo.save()

    clientes = Clientes.objects.only('id', 'nombre')

    return render(request, 'activos/activo-actualizar.html', {'instancia': activo, 'clientes': clientes})


def post(request):
    if request.method == 'POST':
        Activos.objects.create(
            nombre=request.POST['nombre'],
            placa=request.POST.get('placa', None),
            tipo_activo=request.POST['tipo_activo'],
            cliente_id=request.POST['cliente_id'],
        )

    clientes = Clientes.objects.only('id', 'nombre')
        
    return render(request, 'activos/activo-crear.html', {'clientes': clientes}) 


def delete(request, pk):
    activo = get_object_or_404(Activos, pk=pk)
    activo.delete()
    return get(request)