from django.db import models

# Create your models here.
class Paciente(models.Model):
    run = models.CharField(max_length=200, verbose_name="RUN", unique=True)
    dv = models.CharField(max_length=1, verbose_name="Dígito Verificador")
    nombre = models.CharField(max_length=50, verbose_name="Nombres")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-created']

    def __str__(self):
        return self.nombre + ' ' + self.apellidos