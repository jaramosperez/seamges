from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Caso
from .forms import CasoForm
import datetime


# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class CasoListView(ListView):
    model = Caso

@method_decorator(staff_member_required, name='dispatch')
class CasoDetailView(DetailView):
    model = Caso

@method_decorator(staff_member_required, name='dispatch')
class CasoCreateView(CreateView):
    model = Caso
    form_class = CasoForm
    success_url = reverse_lazy('casos:casos')

@method_decorator(staff_member_required, name='dispatch')
class CasoUpdateView(UpdateView):
    model = Caso
    form_class = CasoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('casos:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CasoDeleteView(DeleteView):
    model = Caso
    success_url = reverse_lazy('casos:casos')


