from django.shortcuts import render

def lista_clientes(request):
    contexto = {
        "clientes": [
            {"nombre": "acer"},
            {"nombre": "hp"},
            {"nombre": "sql"},
            {"nombre": "passar.expres"},
            {"nombre": "servioptica"},
            {"nombre": "codabas"},
            {"nombre": "samsung"},
            {"nombre": "LG"},
            {"nombre": "office"},
        ]
    }
    http_response = render(
        request=request,
        template_name='MiOficina/lista_clientes.html',
        context=contexto,
    )
    return http_response

def cargos_disponibles(request):
    contexto = {
        "cargos": [
            {"nombre": "Soporte_Tecnico", "vacantes": 10},
            {"nombre": "Ingeniero_en_Redes", "vacantes": 4},
            {"nombre": "especialista_en_Backup", "vacantes": 2},
            {"nombre": "especialista_en_seguridad", "vacantes": 7},
            {"nombre": "diseñador grafico", "vacantes": 3},
            {"nombre": "programador python", "vacantes": 2},
        ]
    }
    http_response = render(
        request=request,
        template_name='MiOficina/cargos_disponibles.html',
        context=contexto,
    )
    return http_response