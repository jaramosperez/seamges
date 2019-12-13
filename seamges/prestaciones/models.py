from django.db import models

# Create your models here.
class Prestacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Prestación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Prestación"
        verbose_name_plural = "Prestaciones"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

