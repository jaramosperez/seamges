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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Citación"
        verbose_name_plural = "Citaciones"
        ordering = ['-fecha_agenda']


