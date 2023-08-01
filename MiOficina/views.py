from django.shortcuts import render

def cargos_disponibles(request):
    contexto = {
        "cargos": [
            {"nombre": "Soporte_Tecnico", "vacantes": 10},
            {"nombre": "Ingeniero_en_Redes", "vacantes": 4},
            {"nombre": "especialista_en_Backup", "vacantes": 2},
        ]
    }
    http_response = render(
        request=request,
        template_name='MiOficina/cargos_disponibles.html',
        context=contexto,
    )
    return http_response