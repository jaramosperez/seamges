from django.db import models

# Create your models here.
class Profesion(models.Model):
    nombre = models.CharField(max_length=20, unique=True, verbose_name="Nombre de Profesión")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    