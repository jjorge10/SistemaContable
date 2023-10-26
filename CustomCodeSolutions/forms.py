# tuaplicacion/forms.pfrom django import forms
from django import forms
from .models import transaccion, cuenta_transaccion
from django.forms.widgets import DateInput

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = transaccion
        fields = ['num_transaccion', 'fecha','descripcion', 'total_debe_tran', 'total_haber_tran']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
            'num_transaccion': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = cuenta_transaccion
        fields = ['num_transaccion', 'cod_cuenta', 'debe', 'haber']
    
class CuentaForm2(forms.ModelForm):
    class Meta:
        model = cuenta_transaccion
        fields = ['num_transaccion', 'cod_cuenta', 'debe', 'haber']
          


