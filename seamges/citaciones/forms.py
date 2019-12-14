from django import forms
from prestaciones.models import Prestacion
from .models import Citacion
from profesionales.models import Profesional


class CitacionForm(forms.ModelForm):
    ESTADOS_CITACIONES = [
        ('Citado', 'Citado'),
        ('No se presenta', 'No se presenta'),
        ('Realizada', 'Realizada'),
        ('Anulada', 'Anulada'),
    ]
    estado = forms.ChoiceField(choices=ESTADOS_CITACIONES)
    prestacion = forms.ModelChoiceField(queryset=Prestacion.objects.all())
    profesional = forms.ModelChoiceField(queryset=Profesional.objects.all())
    fecha_agenda = forms.DateField()
    observacion = forms.TextInput()

    class Meta:
        model = Citacion
        fields = ['estado', 'prestacion', 'profesional', 'fecha_agenda', 'observacion']
        widgets = {
            'fecha_agenda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'type': 'date', 'id': '#example1'})
        }
