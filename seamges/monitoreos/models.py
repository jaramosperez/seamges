from django.db import models

# Create your models here.
class Monitoreo(models.Model):
    archivo = models.FileField(upload_to='media/%Y/%m/%d/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
