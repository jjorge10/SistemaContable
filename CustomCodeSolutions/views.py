from django.shortcuts import render
from .models import Transacciones
from django.http.response import JsonResponse


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
    return render(request,'CustomCodeSolutions/sistemaCosteo.html')