from rest_framework import serializers
from activos.models import Activos


class ActivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activos
        fields = '__all__'