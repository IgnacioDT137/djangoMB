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
    path('home', home, name='home'),
    path('crudPromos', crudPromos, name='crudPromos'),
    path('addPromos', addPromo, name='addPromos'),
    path('delPromo/<code>', delPromo, name='delPromo'),
    path('editPromo/<code>', editPromo, name='editPromo'),
    #urls del crud
    path('crudProductos', crudProductos, name="crudProductos"),
    path('registroProductos', registroProductos, name="registroProductos"),
    #funciones del crud
    path('añadirProductos/', añadirProductos, name='añadirProductos'),
    path('actualizarProductos/<codigo>', actualizarProductos, name='actualizarProductos'),
    path('editarProductos/', editarProductos, name='editarProductos'),
    path('borrarProductos/<codigo>', borrarProductos, name='borrarProductos'),
    path('crudVentas', ventas, name='crudVentas'),
]