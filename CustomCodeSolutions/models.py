from django.db import models

# Create your models here.

class Transacciones(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    debe = models.FloatField()
    haber = models.FloatField()
 
    class Meta:
        db_table = 'Transacciones'


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
