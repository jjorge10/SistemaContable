# tuaplicacion/forms.pfrom django import forms
from django import forms
from .models import transaccion, cuenta
from django.forms.widgets import DateInput

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = transaccion
        fields = ['num_transaccion', 'descripcion', 'total_debe_tran', 'total_haber_tran']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = cuenta
        fields = ['cod_cuenta', 'id_tipo', 'nombre_cuenta', 'saldo_cuenta', 'id_es', 'total_debe_c', 'total_haber_c']
       


