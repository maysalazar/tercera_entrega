from django.contrib import admin

from MiOficina.models import jefe,empleados, cliente

admin.site.register(jefe)
admin.site.register(cliente)
admin.site.register(empleados)

