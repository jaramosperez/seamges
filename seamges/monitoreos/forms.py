from django import forms
from .models import Monitoreo

class MonitoreoForm(forms.ModelForm):
    class Meta:
        model = Monitoreo
        fields = ['archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'ui action input', 'type':'file'})
        }