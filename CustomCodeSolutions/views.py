from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.forms import formset_factory
from .forms import TransaccionForm, CuentaForm, CuentaForm2
from CustomCodeSolutions import models
from json import dumps


# Create your views here.
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')


def transaccion(request):
    
    CuentaFormSet = formset_factory(CuentaForm, extra=2)
    if request.method == 'POST':
        print(request.POST['num_transaccion'])
        datos={
            'num_transaccion':request.POST['num_transaccion'],
            'fecha':request.POST['fecha'], 
            'descripcion':request.POST['descripcion'], 
            'total_debe_tran':request.POST['form-0-debe'] , 
            'total_haber_tran':request.POST['form-1-haber']
        }
        form=TransaccionForm(datos)
        form.save()
        """form = models.transaccion(datos)
        form.save()
        datos2={
            'num_transaccion':request.POST['num_transaccion'],
            'cod_cuenta':request.POST['form-0-cod_cuenta'],
            'debe':request.POST['form-0-debe'],
            'haber':0
        }
        formct=models.cuenta_transaccion(datos2)
        formct.save()
        datos3={
        'num_transaccion':request.POST['num_transaccion'],
        'cod_cuenta':request.POST['form-1-cod_cuenta'],
        'debe':0,
        'haber':request.POST['form-1-haber']
        }
        formct2=models.cuenta_transaccion(datos3)
        formct2.save()"""
        return redirect('transacciones.html')
    else:
        form = TransaccionForm()
        formct = CuentaFormSet()

    transacciones = models.transaccion.objects.all()
    return render(request, 'transacciones.html', {'form': form, 'formct' : formct,'transacciones': transacciones})
    

def eliminarTransaccion(request, id):
    t = models.transaccion.objects.get(id=id)
    t.delete()

    return redirect('transacciones.html')
    
def catalogo_cuentas(request):
    tipos_cuenta = models.tipo_cuenta.objects.all()
    cuentas = models.cuenta.objects.all()
    return render(request, 'catalogo_cuentas.html', {'tipos_cuenta': tipos_cuenta, 'cuentas': cuentas})


def crearCuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)  # Utiliza CuentaForm, no Cuenta
        if form.is_valid():
            form.save()
            return redirect('crearCuenta.html')  # Reemplaza 'nombre_de_la_vista' con el nombre correcto de la vista
    else:
        form = CuentaForm()

    cuentas = models.transaccion.objects.all()
    return render(request, 'crearCuenta.html', {'form': form, 'cuentas': cuentas})

def estadosFinancieros(request):
    cuentas_balance = models.cuenta.objects.filter(id_es= 1).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')
    cuentas_resultado = models.cuenta.objects.filter(id_es=2).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')
    cuentas_capital = models.cuenta.objects.filter(id_es=3).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')

    dc_balance = {}
    dc_resultado ={}
    pie_resultado={}
    pie_balance={}
    dc_capital = {}
    var = 0
    total_debe_b = 0
    total_haber_b = 0
    total_debe_er = 0
    total_haber_er = 0
    resultado_ejercicio= 0
    for c in cuentas_balance:
        cuenta ={}
        cuenta['cod_cuenta']= c.get('cod_cuenta')
        cuenta['nombre_cuenta']=c.get('nombre_cuenta')
        cuenta['saldo_cuenta']=c.get('saldo_cuenta')
        if c.get('total_debe_c') > c.get('total_haber_c'):
            cuenta['lado_saldo']= "debe"
            total_debe_b=  total_debe_b + c.get('saldo_cuenta')
        else:
            cuenta['lado_saldo']="haber"
            total_haber_b = total_haber_b + c.get('saldo_cuenta')
        dc_balance['cuenta '+ str(var)]=cuenta
        var=var+1
    
    pie_balance['total_debe']=total_debe_b
    pie_balance['total_haber']=total_haber_b

    var=0
    for x in cuentas_resultado:
        cr = {}
        cr['cod_cuenta']= x.get('cod_cuenta')
        cr['nombre_cuenta']=x.get('nombre_cuenta')
        cr['saldo_cuenta']=x.get('saldo_cuenta')
        if x.get('total_debe_c') > x.get('total_haber_c'):
            cr['lado_saldo']= "debe"
            total_debe_er=  total_debe_er + x.get('saldo_cuenta')
        else:
            cr['lado_saldo']="haber"
            total_haber_er = total_haber_er + x.get('saldo_cuenta')
        dc_resultado['cuenta '+ str(var)]=cr
        var=var+1
    pie_resultado['total_debe']=total_debe_er
    pie_resultado['total_haber']=total_haber_er
    resultado_ejercicio = abs(total_debe_er-total_haber_er)
    pie_resultado['resultado_ejerc']=resultado_ejercicio

    if total_debe_er > total_haber_er:
        pie_resultado['lado_resultado']= "debe"
    else:
        pie_resultado['lado_resultado']="haber"


    return render(request, 'CustomCodeSolutions/pruebaes.html',{'datos_balance': dc_balance,'pie_balance':pie_balance ,'datos_resultado':dc_resultado, 'pie_resultado': pie_resultado})

       
