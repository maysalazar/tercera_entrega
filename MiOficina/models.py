from django.db import models

class jefeempresa(models.Model):
    #los atributos de la clase(son las columnas de la tabla)
    nobre_jefe = models.CharField(max_length=120) # define una columna que guarda texto en este caso 64 letras maximas
    apellido_jefe = models.CharField(max_length=120)
    cc_jefe = models.CharField(max_length=32)
    profesion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class empleados(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    cardo_asignado = models.CharField(max_length=120)


class clientes(models.Model):
    nombre_empresa = models.CharField(max_length=120)
    dni = models.CharField(max_length=32)
    nobre_dueñor = models.CharField(max_length=64) # define una columna que guarda texto en este caso 64 letras maximas
    apellido_dueño= models.IntegerField()
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    fecha_inicio_contrato = models.DateTimeField(auto_now_add=True)  # DateTimeField = guarda la fecha y lka hora de entrega
    description_empresa = models.IntegerField()
    
