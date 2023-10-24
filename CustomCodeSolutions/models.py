from pickle import FALSE
from django.db import models


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
    num_transaccion= models.IntegerField(primary_key=True, unique=True, null=False)
    descripcion=models.CharField(max_length=500, null=False)
    fecha= models.DateField(unique=False, null=False)
    total_debe_tran= models.FloatField(null=False)
    total_haber_tran= models.FloatField(null=False)

class cuenta_transaccion(models.Model):
    id_ct= models.AutoField(primary_key=True, unique=True, null=False)
    num_transaccion= models.ForeignKey(transaccion, on_delete=models.CASCADE, null=False)
    cod_cuenta= models.ForeignKey(cuenta, on_delete=models.CASCADE, null=False)
    debe = models.FloatField(null=False)
    haber = models.FloatField(null=False)

