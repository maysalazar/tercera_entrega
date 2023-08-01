from django.contrib import admin
from django.urls import path

from MiOficina.views import cargos_disponibles

#son las urls especificas de la app 

urlpatterns = [
    path('Cargos/', cargos_disponibles),
    
]