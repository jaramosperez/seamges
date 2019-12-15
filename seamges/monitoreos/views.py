from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Monitoreo
from .forms import MonitoreoForm
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import csv
import codecs
from pacientes.models import Paciente
from patologias.models import Patologia
from casos.models import Caso
from establecimientos.models import Establecimiento


# Create your views here.
@method_decorator(login_required, name='dispatch')
class MonitoreoListView(ListView):
    model = Monitoreo


@method_decorator(login_required(), name='dispatch')
class MonitoreoCreateView(CreateView):
    model = Monitoreo
    form_class = MonitoreoForm
    success_url = reverse_lazy('casos:casos')

    def get_success_url(self):
        return reverse_lazy('casos:casos') + '?ok'

#CARGA DE LOS CASOS DESDE EL MONITOREO
@receiver(post_save, sender=Monitoreo)
def ensure_monitoreo_upload(sender, instance, **kwargs):
    arcchivo = instance.archivo.url[1:]
    if kwargs.get('created', False):
        with codecs.open(arcchivo, encoding='utf-8', errors='ignore') as fdata:
            reader = csv.reader(fdata)
            next(reader)  # AVANZA PARA NO CONTAR LOS TITULOS DE LAS COLUMNAS

            # Paciente.objects.all().delete()
            # Patologia.objects.all().delete()
            # Caso.objects.all().delete()

            # RECORRE EL DOCUMENTO FILA POR FILA [YA VIENE EXCLUIDAS LAS CABECERAS]
            for row in reader:
                # REALIZA LA VERIFICACIÓN DE CADA ENTIDAD SI EXISTEN O SI DEBE CREARLAS, SE LE ASIGNAN LAS COLUMNAS A VERIFICAR E IMPORTAR.
                paciente, created = Paciente.objects.get_or_create(
                    run=row[(1)], dv=row[2], nombres=row[4], apellidos=row[3])
                patologia, created = Patologia.objects.get_or_create(nombre=row[0])
                establecimiento, created = Establecimiento.objects.get_or_create(
                    nombre=row[9])

                caso, created = Caso.objects.get_or_create(
                    patologia=patologia, paciente=paciente, fecha_inicio=row[5], fecha_limite=row[6],
                    establecimiento=establecimiento, observacion='')
