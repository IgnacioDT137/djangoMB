from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=14)
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField(max_length=16, null=False)
    telefono = models.IntegerField(null=False)
    email = models.EmailField(null=False, unique=True)
    pwd = models.CharField(null=False, max_length=12)
