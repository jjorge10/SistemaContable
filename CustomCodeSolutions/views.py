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