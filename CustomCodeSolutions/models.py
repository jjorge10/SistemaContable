from django.db import models

class TipoCuenta(models.Model):
    nombre = models.CharField(max_length=50)
    id_tipo = models.AutoField(primary_key=True)
    tiene_cod_cuenta = models.BooleanField()

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    alias = models.CharField(max_length=10)
    tipo = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    saldo = models.FloatField()
    total_debe = models.FloatField()
    total_haber = models.FloatField()

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    descripcion = models.CharField(max_length=500)
    fecha = models.DateField()
    total_debe = models.FloatField()
    total_haber = models.FloatField()
    registra = models.CharField(max_length=500)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
# Create your models here.
