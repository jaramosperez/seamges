from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Caso
from citaciones.models import Citacion
from .forms import CasoForm, CasoUpdateForm
import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
import csv
import codecs

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CasoListView(ListView):
    model = Caso


@method_decorator(login_required, name='dispatch')
class CasoDetailView(DetailView):
    model = Caso


    def get_context_data(self, **kwargs):
        context = super(CasoDetailView, self).get_context_data(**kwargs)
        citaciones_listado = Citacion.objects.filter(caso_id=self.object.id)
        citaciones_nsp = Citacion.objects.filter(caso_id=self.object.id).filter(estado__contains='No se presenta').count()
        hoy = datetime.date.today()
        mensaje_nsp = ''
        cant_nsp = 0

        for citacion in citaciones_listado:
            if citacion.ESTADOS_CITACIONES == 'No se presenta':
                cant_nsp = cant_nsp + 1
                return cant_nsp

        if citaciones_nsp >= 2:
            mensaje_nsp = 'El paciente tiene dos NSP, esta caso debería ser Exceptuado'
        elif citaciones_nsp == 1:
            mensaje_nsp = 'El paciente tiene un NSP, le falta un NSP para ser Exceptuado'
        elif citaciones_nsp == 0:
            mensaje_nsp = 'Este caso puede ser exceptuado con dos NSP'

        vencimiento = self.object.fecha_limite - hoy
        context['mensaje_nsp'] = mensaje_nsp
        context['vencimiento'] = vencimiento.days
        context['citaciones_listado'] = citaciones_listado
        return context


@method_decorator(login_required, name='dispatch')
class CasoCreateView(CreateView):
    model = Caso
    form_class = CasoForm
    success_url = reverse_lazy('casos:casos')


@method_decorator(login_required, name='dispatch')
class CasoUpdateView(UpdateView):
    model = Caso
    form_class = CasoUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('casos:caso', args=[self.object.id]) + '?casook'


@method_decorator(login_required, name='dispatch')
class CasoDeleteView(DeleteView):
    model = Caso
    success_url = reverse_lazy('casos:casos')
