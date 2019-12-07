from django.db import models
from profesiones.models import Profesion

# Create your models here.
class Profesional(models.Model):
    run = models.CharField(max_length=10, verbose_name="RUN")
    nombres = models.CharField(max_length=50, verbose_name="Nombre")
    primer_apellido = models.CharField(max_length=50 , verbose_name="Primer Apellido")
    segundo_apellido = models.CharField(max_length=50 , verbose_name="Segundo Apellido")
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['nombres']

    def __str__(self):
        return self.nombres + ' ' + self.primer_apellido + ' ' + self.segundo_apellido 
    