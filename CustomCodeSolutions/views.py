from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import TransaccionForm, CuentaForm
from .models import *
from .models import TipoCuenta, Cuenta

# Create your views here.
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')


def transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transacciones.html')
    else:
        form = TransaccionForm()

    transacciones = Transaccion.objects.all()
    return render(request, 'transacciones.html', {'form': form, 'transacciones': transacciones})
    

def eliminarTransaccion(request, id):
    t = Transaccion.objects.get(id=id)
    t.delete()

    return redirect('transacciones.html')
    
def catalogo_cuentas(request):
    tipos_cuenta = TipoCuenta.objects.all()
    cuentas = Cuenta.objects.all()
    return render(request, 'catalogo_cuentas.html', {'tipos_cuenta': tipos_cuenta, 'cuentas': cuentas})


def crearCuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)  # Utiliza CuentaForm, no Cuenta
        if form.is_valid():
            form.save()
            return redirect('crearCuenta.html')  # Reemplaza 'nombre_de_la_vista' con el nombre correcto de la vista
    else:
        form = CuentaForm()

    cuentas = Cuenta.objects.all()
    return render(request, 'crearCuenta.html', {'form': form, 'cuentas': cuentas})



       