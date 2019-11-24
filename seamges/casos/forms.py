from django import forms
from .models import Caso

class CasoForm(forms.ModelForm):

    class Meta:
        model = Caso
        fields = ['fecha_inicio', 'fecha_limite', 'observacion']
        widgets = {
            'fecha_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'type': 'date', 'id': '#example1'}),
            'fecha_limite': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'type': 'date', 'id': '#example1'}),
            'observacion': forms.TextInput(attrs={'class':'ui input'})
        }