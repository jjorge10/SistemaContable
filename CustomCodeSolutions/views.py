from django.shortcuts import render, redirect
from .models import Transacciones
from django.http.response import JsonResponse
from .models import Costos_Directos,CostosIndirectos, Mano_de_Obra , Tabla_Final
from django.views.generic.edit import CreateView 
from decimal import Decimal  # Añadir importación Decimal


# Create your views here.
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')

def Transaccion(request):
     transacciones = Transacciones.objects.all()
     return render(request,'CustomCodeSolutions/transaccion.html',{'transaccion': transacciones})

   

def Catalogo(request):
    return render(request,'CustomCodeSolutions/catalogo.html')


def Mayor(request):
    return render(request,'CustomCodeSolutions/mayor.html')

def estadosFinancieros(request):
    return render(request,'CustomCodeSolutions/estadosFinancieros.html')

def SistemaCosteo(request):
    costos_directos = Costos_Directos.objects.all()
    mano_de_obra = Mano_de_Obra.objects.all()
    costos_indirectos = CostosIndirectos.objects.all()


    return render(request,'CustomCodeSolutions/sistemaCosteo.html', {'costos_directos': costos_directos, 'mano_de_obra': mano_de_obra, 'costos_indirectos': costos_indirectos})




def create_costos_directos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        concepto = request.POST['concepto']
        importe = request.POST['importe']

        # Crear un nuevo objeto de costos directos
        costos_directos = Costos_Directos(concepto=concepto, importe=importe)

        # Guardar el objeto de costos directos en la base de datos
        costos_directos.save()


        # Redireccionar al usuario a la página principal
        return redirect('/Sistemacosteo/')

    
    
    return render(request, 'costos_directos/create.html')


def create_mano_de_obra(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        trabajador = request.POST['trabajador']
        horas_trabajas = request.POST['horas_trabajadas']
        costo_hora = request.POST['costo_hora']

        total_trabajador =  int(horas_trabajas)* int(costo_hora)


        # Crear un nuevo objeto de costos directos
        mano_de_obra = Mano_de_Obra(nombre_del_trabajador=trabajador ,tiempo_de_trabajo= horas_trabajas,costo_por_hora=costo_hora, Total_Trabajador=total_trabajador )

        # Guardar el objeto de costos directos en la base de datos
        mano_de_obra.save()

        # Redireccionar al usuario a la página principal
        return redirect('/Sistemacosteo/')

    return render(request, 'mano_de_obra/create.html')


def create_costos_indirectos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        importe = request.POST['importe']
        # Crear un nuevo objeto de costos directos
        costo_indirectos = CostosIndirectos(importe=importe)
        # Guardar el objeto de costos directos en la base de datos
        costo_indirectos.save()

        # Redireccionar al usuario a la página principal
        return redirect('/Sistemacosteo/')

    return render(request, 'costos_inderectos/create.html')




def create_tabla_final(request):
    if request.method == 'POST':
        fecha_ex = request.POST['fecha-ex']
        producto = request.POST['producto']
        cliente = request.POST['cliente']

        # Obtener costos directos
        costos_directos = Costos_Directos.objects.all()
        suma_costo = Decimal(0)  # Inicializar como Decimal

        for costo_d in costos_directos:     
            suma_costo += costo_d.importe

        # Obtener costo de mano de obra
        costo_mano = Mano_de_Obra.objects.all()
        suma_mano = Decimal(0)  # Inicializar como Decimal

        for mano in costo_mano:
            suma_mano += mano.Total_Trabajador

        # Obtener costos indirectos
        costos_indirectos = CostosIndirectos.objects.all()
        suma_indirectos = Decimal(0)  # Inicializar como Decimal

        for costos_i in costos_indirectos:
            suma_indirectos += costos_i.as_decimal()  # Convertir a número decimal antes de sumar

        # Calcular el costo total
        costo_total = suma_costo + suma_mano + suma_indirectos

        # Crear y guardar la tabla final
        tabla_final = Tabla_Final(fecha=fecha_ex, producto=producto, cliente=cliente, costos_directos=suma_costo, mano_de_obra=suma_mano, costos_indirectos=suma_indirectos, costo_total=costo_total)
        tabla_final.save()

        return redirect('/Sistemacosteo/')

    return render(request, 'costo_total/create.html')




