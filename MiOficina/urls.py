from django.contrib import admin
from django.urls import path

from MiOficina.views import lista_clientes, cargos_disponibles

#son las urls especificas de la app 

urlpatterns = [
    path('clientes/', lista_clientes, name="lista_clientes"),
    path('cargos/', cargos_disponibles, name="cargos_disponibles"),
]