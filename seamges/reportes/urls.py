from django.urls import path
from .views import ReporteListView

reportes_patterns = ([
    path('', ReporteListView.as_view(), name='reportes'),
], 'reportes')