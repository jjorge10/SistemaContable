from django.shortcuts import render
from CustomCodeSolutions import models
from json import dumps

# Create your views here.
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')

def Transacciones(request):
    cuentas= models.cuenta.objects.all().values('cod_cuenta', 'nombre_cuenta')
    c = {}
    var =0
    for cuenta in cuentas:
        x = {}
        nombre = cuenta.get('nombre_cuenta')
        codigo = cuenta.get('cod_cuenta')
        x['cod_cuenta']= codigo
        x['nombre_cuenta']=nombre
        c['cuenta'+str(var)]=x
        var=var+1
    
    datos_cuentas = dumps(c)

    datos_c= {'datos' : datos_cuentas}

    return render(request,'CustomCodeSolutions/transacciones.html', datos_c)

def Catalogo(request):
    cuentas = models.cuenta.objects.all().values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta')
    c = {}
    var =0
    for cuenta in cuentas:
        x = {}
        nombre = cuenta.get('nombre_cuenta')
        codigo = cuenta.get('cod_cuenta')
        saldo = cuenta.get('saldo_cuenta')
        x['cod_cuenta']= codigo
        x['nombre_cuenta']=nombre
        x['saldo_cuenta']= saldo
        c['cuenta'+str(var)]=x
        var=var+1
    
    datos_cuentas = dumps(c)

    datos_c= {'datos' : datos_cuentas}

    return render(request, 'CustomCodeSolutions/pruebacatalogo.html', datos_c )

    
def estadosFinancieros(request):
    cuentas_balance = models.cuenta.objects.filter(id_es= 1).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')
    cuentas_resultado = models.cuenta.objects.filter(id_es=2).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')
    cuentas_capital = models.cuenta.objects.filter(id_es=3).values('cod_cuenta', 'nombre_cuenta', 'saldo_cuenta', 'total_debe_c', 'total_haber_c')

    dc_balance = {}
    dc_resultado ={}
    dc_capital = {}
    total_debe_b = 0
    total_haber_b = 0
    for c in cuentas_balance:
        cuenta ={}
        cuenta['cod_cuenta']= c.get('cod_cuenta')
        cuenta['nombre_cuenta']=c.get('nombre_cuenta')
        cuenta['saldo_cuenta']=c.get('saldo_cuenta')
        if c.get('total_debe_c') > c.get('total_haber_c'):
            cuenta['lado_saldo']= "debe"
            total_debe_b=  total_debe_b + c.get
        else:
            cuenta['lado_saldo']="haber"
        


