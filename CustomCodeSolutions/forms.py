# tuaplicacion/forms.pfrom django import forms
from django import forms
from .models import transaccion, cuenta_transaccion, cuenta
from django.forms.widgets import DateInput

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = transaccion
        fields = ['num_transaccion', 'fecha','descripcion', 'total_debe_tran', 'total_haber_tran']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date', 'class': 'form-control' }),
            'num_transaccion': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CuentaForm(forms.ModelForm):
    class Meta:
        model = cuenta_transaccion
        fields = ['num_transaccion', 'cod_cuenta', 'debe', 'haber']
        widgets = {
            'num_transaccion': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'cod_cuenta': forms.Select(attrs={'class': 'form-control'}),
            'debe': forms.NumberInput(attrs={'class': 'form-control'}),
            'haber': forms.NumberInput(attrs={'class': 'form-control'}),
        }


    
class CuentaForm2(forms.ModelForm):
    class Meta:
        model = cuenta_transaccion
        fields = ['num_transaccion', 'cod_cuenta', 'debe', 'haber']
          


