from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría.")

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la zona.")

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    consumo_maximo_w = models.IntegerField(help_text="Consumo máximo permitido en Watts.")
    estado = models.BooleanField(default=True, help_text="Indica si el dispositivo está activo.")

    def __str__(self):
        return f"{self.nombre} ({self.zona.nombre})"
