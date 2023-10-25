from django.shortcuts import render, redirect
from .models import Transacciones
from django.http.response import JsonResponse
from .models import Costos_Directos,CostosIndirectos, Mano_de_Obra     
from django.views.generic.edit import CreateView 



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

    return render(request,'CustomCodeSolutions/sistemaCosteo.html')




def create_costos_directos(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        concepto = request.POST['concepto']
        importe = request.POST['importe']

        # Crear un nuevo objeto de costos directos
        costos_directos = Costos_Directos(concepto=concepto, importe=importe)

        # Guardar el objeto de costos directos en la base de datos
        costos_directos.save()

        # Obtener todos los datos de costos directos de la base de datos
        costeo_directo = Costos_Directos.objects.all()

        # Redireccionar al usuario a la página principal
        return redirect('/Sistemacosteo/')

    # Pasar el contexto 'costeo_directo' a la plantilla
    context = {'costeo_directo': costeo_directo}
    return render(request, 'costos_directos/create.html', context)

def mostrar_costo_directo(request):
    costeo_directo = Costos_Directos.objects.all()
    costeo_datos = {'costeo_directo': costeo_directo}
    return render(request, 'CustomCodeSolutionssistemaCosteo.html', costeo_datos)



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