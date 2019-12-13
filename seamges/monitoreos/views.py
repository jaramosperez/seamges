from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Monitoreo
from .forms import MonitoreoForm


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
