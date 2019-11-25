from django import forms
from prestaciones.models import Prestacion
from profesionales.models import Profesional
from .models import Citacion


class CitacionForm(forms.ModelForm):
    prestacion = forms.ModelChoiceField(queryset=Prestacion.objects.all())
    profesional = forms.ModelChoiceField(queryset=Profesional.objects.all())
    class Meta:
        model = Citacion
        fields = ['prestacion', 'profesional','fecha_agenda']
        widgets = {
            'fecha_agenda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'type': 'date', 'id': '#example1'})
        }
