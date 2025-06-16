# admin.py
from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'tipo_documento', 'numero_documento', 'cargo')
    search_fields = ('nombre_completo', 'numero_documento')
    list_filter = ('tipo_documento', 'jornada')