from django.urls import path
from .views import CitacionCreateView, CitacionUpdateView

citaciones_patterns = ([
    path('create/<caso_id>/', CitacionCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CitacionUpdateView.as_view(), name='update')
],'citaciones')