from django.db import models

# Create your models here.
class Monitoreo(models.Model):
    archivo = models.FileField(upload_to='media/%Y/%m/%d/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de primer monitoreo")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de último monitoreo")

    class Meta:
        verbose_name = "Monitoreo"
        verbose_name_plural = "Monitoreos"
        ordering = ['created']