from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=14)
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField(max_length=16, null=False)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(null=False, unique=True)
    pwd = models.CharField(null=False, max_length=12)

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField(max_length=20)
    stock = models.IntegerField(max_length=20)
    imagen = models.CharField(max_length=500, default= "imagen")

class Reserva_mantencion(models.Model):
    id_mantencion = models.AutoField(primary_key=True)
    usuario = models.EmailField(null=False)
    tipo_bici = models.CharField(max_length=30)
    tipo_mantencio = models.CharField(max_length=30)
    detalles = models.CharField(max_length=1000)

class Reserva_arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True)
    tipo_bici = models.CharField(max_length=30)
    tiempo_arriendo = models.CharField(max_length=30)
    tipo_garantia = models.CharField(max_length=30)
    usuario = models.EmailField(null=False)
