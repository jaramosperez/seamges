from django.db import models
from pacientes.models import Paciente
from patologias.models import Patologia

# Create your models here.
class Caso(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    patologia = models.ForeignKey(Patologia, on_delete=models.CASCADE, verbose_name="Patología")
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio")
    fecha_limite = models.DateField(verbose_name="Fecha Límite")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Caso"
        verbose_name_plural = "Casos"
        ordering = ['-fecha_limite']