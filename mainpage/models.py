from django.db import models

# Create your models here.

class Aporte(models.Model):
    tipo = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.tipo

class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=200, primary_key=True)
    email = models.CharField(max_length=200, null=True)
    fono = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    representante = models.CharField(max_length=200)
    fono = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    rut = models.ForeignKey(Empleado, on_delete=models.SET_NULL)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    aporte = models.ForeignKey(Aporte, on_delete=models.SET_NULL)
    inicio = models.DateField()
    final = models.DateField()
