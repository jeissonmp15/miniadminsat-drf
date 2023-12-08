from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    nombre_contacto = models.CharField(max_length=80)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        unique_together = ('nombre', 'nit')

