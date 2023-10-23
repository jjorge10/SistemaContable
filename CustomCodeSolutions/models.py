from django.db import models

# Create your models here.

class Transacciones(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    debe = models.FloatField()
    haber = models.FloatField()
 
    class Meta:
        db_table = 'Transacciones'