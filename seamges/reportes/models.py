from django.db import models

# Create your models here.
class Reporte(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del reporte")
    descripcion = models.TextField(verbose_name="Descripción del reporte")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['nombre']