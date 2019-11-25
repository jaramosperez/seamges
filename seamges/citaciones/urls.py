from django.urls import path
from .views import CitacionCreateView

citaciones_patterns = ([
    path('create/<caso_id>/', CitacionCreateView.as_view(), name='create')
],'citaciones')