from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.forms import formset_factory
from .forms import TransaccionForm, CuentaForm, CuentaForm2
from CustomCodeSolutions import models
from json import dumps
from decimal import Decimal  # Añadir importación Decimal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.
@login_required
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')

def login(request):

    return render(request,'registration/login.html')

def exit(request):
    logout(request)
    return redirect('inicio')

@login_required
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
    
@login_required
def eliminarTransaccion(request, numero_transaccion):
    t = models.transaccion.objects.get(id=numero_transaccion)
    t.delete()

    return redirect('transacciones.html')
@login_required   
def catalogo_cuentas(request):
    tipos_cuenta = models.tipo_cuenta.objects.all()
    cuentas = models.cuenta.objects.all()
    return render(request, 'catalogo_cuentas.html', {'tipos_cuenta': tipos_cuenta, 'cuentas': cuentas})

@login_required
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
@login_required
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
@login_required
def SistemaCosteo(request):
    costos_directos = models.Costos_Directos.objects.all()
    mano_de_obra = models.Mano_de_Obra.objects.all()
    costos_indirectos = models.CostosIndirectos.objects.all()
    tabla  = models.Tabla_Final.objects.all()


    return render(request,'sistemaCosteo.html', {'costos_directos': costos_directos, 'mano_de_obra': mano_de_obra, 'costos_indirectos': costos_indirectos, 'tabla': tabla})
@login_required
def create_tabla_final(request):
    if request.method == 'POST':
        fecha_ex = request.POST['fecha-ex']
        productox = request.POST['producto']
        clientex = request.POST['cliente']

        # Obtener costos directos
        suma_costo = models.Costos_Directos.objects.aggregate(total_importes=Sum('importe'))['total_importes']

        # Obtener costo de mano de obra
        suma_mano = models.Mano_de_Obra.objects.aggregate(total_mano_de_obra=Sum('Total_Trabajador'))['total_mano_de_obra'] or 0

        # Obtener costos indirectos
        costos_indirectos = models.CostosIndirectos.objects.all()
        suma_indirectos = costos_indirectos.aggregate(total=Sum('importe'))['total'] or Decimal(0)

        # Calcular el costo total
        costo_total = suma_costo + suma_mano + suma_indirectos

        # Crear y guardar la tabla final
        tabla_final = models.Tabla_Final(fecha=fecha_ex, producto=productox, cliente=clientex, costos_directos=suma_costo, mano_de_obra=suma_mano, costos_indirectos=suma_indirectos, costo_total=costo_total)
        tabla_final.save()
        models.Costos_Directos.objects.all().delete()
        models.Mano_de_Obra.objects.all().delete()
        models.CostosIndirectos.objects.all().delete()

        return redirect('/sistemaCosteo/')
    
    return render(request, 'CustomCodeSolutions/sistemaCosteo.html')
@login_required
def create_costos_directos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        concepto = request.POST['concepto']
        importe = request.POST['importe']

        # Crear un nuevo objeto de costos directos
        costos_directos = models.Costos_Directos(concepto=concepto, importe=importe)

        # Guardar el objeto de costos directos en la base de datos
        costos_directos.save()


        # Redireccionar al usuario a la página principal
        return redirect('/sistemaCosteo/')

    
    
    return render(request, 'costos_directos/create.html')

@login_required
def create_mano_de_obra(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        trabajador = request.POST['trabajador']
        horas_trabajas = request.POST['horas_trabajadas']
        costo_hora = request.POST['costo_hora']

        total_trabajador =  int(horas_trabajas)* int(costo_hora)


        # Crear un nuevo objeto de costos directos
        mano_de_obra = models.Mano_de_Obra(nombre_del_trabajador=trabajador ,tiempo_de_trabajo= horas_trabajas,costo_por_hora=costo_hora, Total_Trabajador=total_trabajador )

        # Guardar el objeto de costos directos en la base de datos
        mano_de_obra.save()

        # Redireccionar al usuario a la página principal
        return redirect('/sistemaCosteo/')

    return render(request, 'mano_de_obra/create.html')

@login_required
def create_costos_indirectos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        importe = request.POST['importe']
        # Crear un nuevo objeto de costos directos
        costo_indirectos = models.CostosIndirectos(importe=importe)
        # Guardar el objeto de costos directos en la base de datos
        costo_indirectos.save()

        # Redireccionar al usuario a la página principal
        return redirect('/sistemaCosteo/')

    return render(request, 'costos_inderectos/create.html')
