from django.contrib import admin
from .models import Transacciones, Costos_Directos, CostosIndirectos,Mano_de_Obra, Tabla_Final

# Register your models here.

admin.site.register(Transacciones)
admin.site.register(Costos_Directos)
admin.site.register(CostosIndirectos)
admin.site.register(Mano_de_Obra)
admin.site.register(Tabla_Final)