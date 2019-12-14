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
        hoy = datetime.date.today()
        vencimiento = self.object.fecha_limite - hoy
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        citaciones_listado = Citacion.objects.filter(caso_id=self.object.id)
        hoy = datetime.date.today()
        vencimiento = self.object.fecha_limite - hoy
        context['vencimiento'] = vencimiento.days
        context['citaciones_listado'] = citaciones_listado
        context['form'] = self.form_class
        return context

    def get_success_url(self):
        return reverse_lazy('casos:update', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class CasoDeleteView(DeleteView):
    model = Caso
    success_url = reverse_lazy('casos:casos')
