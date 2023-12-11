from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from equipos.models import Equipo


class EquiposSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class EquiposSelectSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'imei']


class EquiposDetailSerializer(ModelSerializer):
    activo_nombre = serializers.ReadOnlyField(source='activo.nombre')
    activo_placa = serializers.ReadOnlyField(source='activo.placa')

    class Meta:
        model = Equipo
        fields = '__all__'