from django.db import models

class Cargos(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class jefe(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class cliente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    nombre_empresa = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class empleados(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

