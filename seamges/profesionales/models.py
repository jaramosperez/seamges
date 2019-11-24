from django.db import models
from profesiones.models import Profesion

# Create your models here.
class Profesional(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Profesional")
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    