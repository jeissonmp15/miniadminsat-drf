from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from clientes.models import Clientes
from rest_framework.views import APIView
from clientes.serializers import ClientesSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class ClientesAPIView(APIView):
    model = Clientes
    serializer_class = ClientesSerializer
    # permission_classes = [AllowAny]

    def get(self, request):
        queryset = self.model.objects.all()
        if request.query_params.get('pk'):
            instance = get_object_or_404(queryset, pk=request.query_params['pk'])
            serializer = self.serializer_class(instance)
        else:
            serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.headers)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk=None):
        pass