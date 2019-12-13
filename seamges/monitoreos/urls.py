from django.urls import path
from .views import MonitoreoListView
from .views import MonitoreoCreateView

monitoreos_patterns = ([
    path('', MonitoreoListView.as_view(), name='monitoreos'),
    path('create/', MonitoreoCreateView.as_view(), name='create'),
],'monitoreos')