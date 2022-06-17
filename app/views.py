import email
from django.shortcuts import render
#importacion del modulo de mensajes 
from django.contrib import messages
#importacion de los modelos en models.py
from .models import *

# Create your views here.

def registro(request):
    if request.method == 'POST':
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['email']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
            newUser = Usuario(
                rut = request.POST['rut'],
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                telefono = request.POST['telefono'],
                email = request.POST['correo'],
                pwd = request.POST['password']
            )

            #se guarda el nuevo usuario en la base de datos
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
    return render(request, 'app/registro.html')