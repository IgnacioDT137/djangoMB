from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario)

admin.site.register(Producto)

admin.site.register(Reserva_mantencion)

admin.site.register(Reserva_arriendo)

admin.site.register(Carrito)

admin.site.register(CarritoItem)

admin.site.register(Venta)

admin.site.register(Notificacion)