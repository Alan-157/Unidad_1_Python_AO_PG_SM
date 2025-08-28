from django.db import models
from django.utils import timezone


x
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

