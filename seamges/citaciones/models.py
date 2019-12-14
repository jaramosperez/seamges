from django.db import models
from profesionales.models import Profesional
from prestaciones.models import Prestacion
from casos.models import Caso

# Create your models here.
class Citacion(models.Model):
    prestacion = models.ForeignKey(Prestacion, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    fecha_agenda = models.DateTimeField(verbose_name="Fecha en Agenda", auto_now=False)
    observacion = models.TextField(verbose_name="Observación Citación", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    ESTADOS_CITACIONES = [
        ('Citado', 'Citado'),
        ('No se presenta', 'No se presenta'),
        ('Realizada', 'Realizada'),
        ('Anulada', 'Anulada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_CITACIONES, default='Citado')

    class Meta:
        verbose_name = "Citación"
        verbose_name_plural = "Citaciones"
        ordering = ['-fecha_agenda']


