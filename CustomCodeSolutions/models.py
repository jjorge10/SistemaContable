from pickle import FALSE
from django.db import models

def get_default_value():
    # Calcula el valor por defecto consultando el valor más alto en la tabla
    last_record = transaccion.objects.aggregate(models.Max('num_transaccion'))
    last_value = last_record['num_transaccion__max'] or 0  # En caso de que no haya registros
    return last_value + 1


# Create your models here.
class tipo_cuenta(models.Model):
    id_tipo= models.AutoField(primary_key=True, unique=True, null=False)
    nom_tipo= models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nom_tipo
    
class tipo_esfinanciero(models.Model):
    id_es=models.AutoField(primary_key=True, unique=True, null= False)
    nom_es= models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nom_es
    
    
class cuenta(models.Model):
    #id= models.AutoField(unique=True, primary_key=False)
    cod_cuenta=models.CharField(primary_key=True, max_length=10, null=False)
    id_tipo= models.ForeignKey(tipo_cuenta, on_delete=models.CASCADE, null=False)
    nombre_cuenta= models.CharField(max_length=50, null=False)
    saldo_cuenta= models.FloatField(null=False)
    id_es=models.ForeignKey(tipo_esfinanciero, on_delete=models.CASCADE ,null= False)
    total_debe_c = models.FloatField(null=False)
    total_haber_c = models.FloatField(null=False)

    def __str__(self):
        return self.nombre_cuenta

class transaccion(models.Model):
    num_transaccion= models.IntegerField(primary_key=True, unique=True, null=False, default=get_default_value)
    descripcion=models.CharField(max_length=500, null=False)
    fecha= models.DateField(unique=False, null=False)
    total_debe_tran= models.FloatField(null=False)
    total_haber_tran= models.FloatField(null=False)

class cuenta_transaccion(models.Model):
    id_ct= models.AutoField(primary_key=True, unique=True, null=False)
    num_transaccion= models.ForeignKey(transaccion, on_delete=models.CASCADE, null=False)
    cod_cuenta= models.ForeignKey(cuenta, on_delete=models.CASCADE, null=False)
    debe = models.FloatField(null=False,default=0.0)
    haber = models.FloatField(null=False, default=0.0)


#################
class Costos_Directos(models.Model):
    concepto = models.CharField(max_length=255,null=False)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.concepto
    class Meta:
        db_table = "costos_directos"


class Mano_de_Obra(models.Model):
    nombre_del_trabajador = models.CharField(max_length=255,null=False)
    tiempo_de_trabajo = models.DecimalField(max_digits=10, decimal_places=2)
    costo_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    Total_Trabajador = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nombre_del_trabajador
    class Meta:
        db_table = "mano_de_obra"

class CostosIndirectos(models.Model):
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.importe}"
    class Meta:
        db_table = "costos_indirectos"


class Tabla_Final(models.Model):
    fecha = models.CharField(max_length=15)
    producto = models.CharField(max_length=255)
    cliente =  models.CharField(max_length=255)
    costos_directos = models.DecimalField(max_digits=10, decimal_places=2)
    mano_de_obra = models.DecimalField(max_digits=10, decimal_places=2)
    costos_indirectos = models.DecimalField(max_digits=10, decimal_places=2)
    costo_total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.fecha}"
    class Meta:
        db_table = "tabla_final"

