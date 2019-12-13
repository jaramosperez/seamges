from django.db import models
from pacientes.models import Paciente
from patologias.models import Patologia
from establecimientos.models import Establecimiento
import datetime

# Create your models here.
class Caso(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    patologia = models.ForeignKey(Patologia, on_delete=models.CASCADE, verbose_name="Patología")
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE,  verbose_name="Establecimiento Responsable")
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio")
    fecha_limite = models.DateField(verbose_name="Fecha Límite")
    observacion = models.TextField(verbose_name='Observación')
    vigente = models.BooleanField(verbose_name='Caso Vigente', default=True)
    exceptuado = models.BooleanField(verbose_name='Caso Exceptuado', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Caso"
        verbose_name_plural = "Casos"
        ordering = ['fecha_limite']

    @property
    def vencimiento(self):
        hoy = datetime.date.today()
        vencimiento = self.fecha_limite - hoy
        return vencimiento.days
