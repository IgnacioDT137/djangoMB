from django.urls import path
from .views import *

urlpatterns = [
    path('',login, name='login'),
    path('registro', registro, name='registro'),
    path('tienda', tienda, name="tienda"),  
    path('producto/<prod_id>', producto, name='producto'),
    path('arriendo-form', arr_form, name='arriendo-form'),
    path('mantencion-form', mant_form, name="mantencion-form"),
    path('agregarproducto/<user_id>/<prod_id>', agregarProducto, name='add'),   
    path('carrito', carrito, name='carrito'),
    path('comprar/<p_total>/<id_carrito>', comprar, name='comprar'),
    path('multicompra/<prod_id>/<user_id>', multiCompra, name="multicompra"),
]