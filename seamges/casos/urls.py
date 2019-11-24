from django.urls import path
from .views import CasoListView, CasoDetailView, CasoCreateView, CasoUpdateView, CasoDeleteView

casos_patterns = ([
    path('', CasoListView.as_view(), name='casos'),
    path('<int:pk>/', CasoDetailView.as_view(), name='caso'),
    path('create/', CasoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CasoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CasoDeleteView.as_view(), name='delete')
], 'casos')