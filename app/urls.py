from django.urls import path
from .views import *

urlpatterns = [
    path('',login, name='login'),
    path('registro', registro, name='registro'),
    path('tienda', tienda, name="tienda"),  
    path('producto/<prod_id>', producto, name='producto'),
    path('arriendo-form', arr_form, name='arriendo-form'),
    path('mantencion-form', mant_form, name="mantencion-form")
    ##,path('insert_mantencion', insert_mantencion, name="insert_mantencion")
    
]