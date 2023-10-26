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
from django.urls import path, include
from CustomCodeSolutions import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.Inicio,name='inicio'),
    path('catalogo_cuentas/', views.catalogo_cuentas, name='catalogo_cuentas'),
    path('transacciones/', views.transaccion, name='transacciones.html'),
    path('eliminarTransaccion/<numero_transaccion>/', views.eliminarTransaccion, name='eliminarTransaccion'),
    path('crearCuenta/', views.crearCuenta, name='crearCuenta.html'),
    path('sistemaCosteo/',views.SistemaCosteo, name='sistemaCosteo.html'),
    path('sistemaCosteo/', TemplateView.as_view(template_name='sistemaCosteo'), name='sistemaCosteo'),
    path('create_costos_directos/', views.create_costos_directos, name='create_costos_directos'),
    path('create_mano_de_obra/', views.create_mano_de_obra, name='create_mano_de_obra'),
    path('create_costos_indirectos/', views.create_costos_indirectos, name='create_costos_indirectos'),
    path('create_tabla_final/',views.create_tabla_final,name='create_tabla_final'),
     path('login/', views.login, name='login'),
    path('logout/',views.exit,name='exit'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
