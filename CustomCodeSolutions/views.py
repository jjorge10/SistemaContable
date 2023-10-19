from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'CustomCodeSolutions/inicio.html')

def Transacciones(request):
    return render(request,'CustomCodeSolutions/transacciones.html')