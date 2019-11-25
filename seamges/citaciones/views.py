from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Citacion
from .forms import CitacionForm
from casos.models import Caso
from prestaciones.models import Prestacion

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class CitacionCreateView(CreateView):
    model = Citacion
    form_class = CitacionForm
    success_url = reverse_lazy('casos:casos')

    # IDENTIFICAR EL CASO AL QUE SE LE AGREGARÁ LA CITACIÓN.
    def form_valid(self, form):
        caso_id = self.kwargs['caso_id']
        form.instance.caso = Caso.objects.get(id=caso_id)
        return super(CitacionCreateView, self).form_valid(form)

    # OBTENER LOS DATOS PARA EL CASO SELECCIONADO.
    def get_context_data(self, **kwargs):
        context = super(CitacionCreateView, self).get_context_data(**kwargs)
        caso_id = self.kwargs['caso_id']
        caso = Caso.objects.get(id=caso_id)
        context['caso'] = caso
        return context

    def get_success_url(self):
        return reverse_lazy('casos:caso', args=[self.object.caso.id]) + '?ok'
