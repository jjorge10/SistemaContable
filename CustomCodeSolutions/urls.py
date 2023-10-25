from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('Transaccion/', views.Transaccion, name="transaccion"),
    path('Transaccion/', TemplateView.as_view(template_name='transaccion.html'), name='transaccion'),
    path('Mayor/',views.Mayor, name="mayor"),
    path('Mayor/', TemplateView.as_view(template_name='mayor.html'), name='mayor'),
    path('Catalogo/', views.Catalogo, name="catalogo"),
    path('Catalogo/', TemplateView.as_view(template_name='catalogo.html'), name='catalogo'),
    path('Estadosfinancieros/',views.estadosFinancieros, name='estadosFinancieros'),
    path('Estadosfinancieros/', TemplateView.as_view(template_name='estadosFinancieros.html'), name='estadosFinancieros'),
    path('Sistemacosteo/',views.SistemaCosteo, name='sistemaCosteo'),
    path('Sistemacosteo/', TemplateView.as_view(template_name='sistemaCosteo.html'), name='sistemaCosteo'),
    path('create_costos_directos/', views.create_costos_directos, name='create_costos_directos'),
    path('create_mano_de_obra/', views.create_mano_de_obra, name='create_mano_de_obra'),
    path('create_costos_indirectos/', views.create_costos_indirectos, name='create_costos_indirectos'),
        
]
