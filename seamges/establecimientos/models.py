from django.db import models

# Create your models here.
class Establecimiento(models.Model):
    nombre = models.CharField(verbose_name="Nombre de establecimiento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Establecimiento"
        verbose_name_plural = "Establecimientos"
        ordering = ['nombre']