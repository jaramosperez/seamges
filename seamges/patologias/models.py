from django.db import models

# Create your models here.
class Patologia(models.Model):
    nombre = models.CharField(max_length=128, unique=True, verbose_name="Nombre de Patología")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Patología"
        verbose_name_plural = "Patologías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre