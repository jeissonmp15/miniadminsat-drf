from enum import unique
from random import choices
from django.db import models

# Create your models here.

class Activos(models.Model):
    class TipoActivo(models.IntegerChoices):
        PERSONAL = 0
        VEHICULAR = 1

    nombre = models.CharField(max_length=50, unique=True)
    placa = models.CharField(max_length=50, null=True)
    tipo_activo = models.IntegerField(choices=TipoActivo.choices)
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.CASCADE, related_name='clientes_activos_set')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'