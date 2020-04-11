from django import forms
from .models import MultasEstacionamiento

class MultasEstacionamientoForm(forms.ModelForm):

    class Meta:
        model = MultasEstacionamiento
        fields = ('patente', 'lugar', 'pagada', 'inspectorid')