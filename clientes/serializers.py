from rest_framework import serializers
from clientes.models import Clientes


class ClientesSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        print('Entra despues del serializer.save() va a actualizar')
        print(validated_data)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        print('Entra despues del serializer.save() va a crear')
        print(validated_data)
        return super().create(validated_data)

    class Meta:
        model = Clientes
        fields = '__all__'