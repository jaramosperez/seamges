from django.shortcuts import render
from .models import Reporte
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ReporteListView(ListView):
    model = Reporte