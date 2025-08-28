from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
from django.db import models
from django.utils import timezone

from .models import Dispositivo

# Modelo para registrar el consumo histórico de un dispositivo
class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    consumo_w = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Medición de {self.dispositivo.nombre} - {self.consumo_w}W"

# Modelo para registrar alertas cuando el consumo excede el límite
class Alerta(models.Model):
    medicion = models.OneToOneField(Medicion, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    revisada = models.BooleanField(default=False, help_text="Indica si la alerta ha sido revisada.")

    def __str__(self):
        return f"Alerta para {self.medicion.dispositivo.nombre}"
