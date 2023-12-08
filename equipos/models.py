from enum import unique
from django.db import models

# Create your models here.
class Equipo(models.Model):
    imei = models.CharField(max_length=16, unique=True)
    simcard = models.PositiveIntegerField(null=True)
    operador = models.CharField(max_length=50, null=True)
    activo = models.ForeignKey('activos.Activos', on_delete=models.SET_NULL, null=True, related_name='equipos_activo_set')
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.CASCADE, related_name='equipos_cliente_set')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

