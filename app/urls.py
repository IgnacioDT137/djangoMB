from django.urls import path
from .views import *

urlpatterns = [
    path('', registro, name='registro'),
    path('tienda', tienda, name="tienda"),  
]