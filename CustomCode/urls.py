"""
URL configuration for CustomCode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CustomCodeSolutions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio,name='inicio'),
    path('catalogo_cuentas/', views.catalogo_cuentas, name='catalogo_cuentas'),
    path('transacciones/', views.transaccion, name='transacciones.html'),
    path('eliminarTransaccion/<id>/', views.eliminarTransaccion, name='eliminarTransaccion'),
    path('crearCuenta/', views.crearCuenta, name='crearCuenta.html'),

]
