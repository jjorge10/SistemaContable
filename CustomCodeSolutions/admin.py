from django.contrib import admin
from CustomCodeSolutions.models import *
# Register your models here.

admin.site.register(cuenta)
admin.site.register(tipo_cuenta)
admin.site.register(tipo_esfinanciero)
admin.site.register(Costos_Directos)
admin.site.register(CostosIndirectos)
admin.site.register(Mano_de_Obra)
admin.site.register(Tabla_Final)