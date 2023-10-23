# tuaplicacion/forms.pfrom django import forms
from django import forms
from .models import Transaccion, Cuenta
from django.forms.widgets import DateInput

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['descripcion', 'fecha', 'total_debe', 'total_haber', 'registra', 'cuenta']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre', 'alias', 'tipo', 'saldo', 'total_debe', 'total_haber']
       


