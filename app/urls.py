from django.urls import path
from .views import *

urlpatterns = [
    path('',login, name='login'),
    path('registro', registro, name='registro'),
    path('tienda', tienda, name="tienda"),  
    path('producto/<prod_id>', producto, name='producto'),
]