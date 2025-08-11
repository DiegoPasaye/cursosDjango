from django.contrib import admin
from .models import Curso, Actividad
from django.utils.html import format_html 

class AdministrarCurso(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'duracion_horas',
        'precio',
        'activo',
        'fecha_creacion',
    )
    ordering = ('fecha_creacion',)
    search_fields = ('nombre', 'descripcion', 'categoria')
    date_hierarchy = 'fecha_creacion'
    list_filter = ('activo', 'categoria', 'precio')


class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id_actividad', 'nombre_actividad', 'curso', 'fecha_creacion')
    list_display_links = ('id_actividad', 'nombre_actividad')
    search_fields = ('nombre_actividad', 'descripcion_actividad', 'curso__nombre')
    list_filter = ('curso', 'fecha_creacion')
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ('fecha_creacion', 'id_actividad')


admin.site.register(Curso, AdministrarCurso)
admin.site.register(Actividad, AdministrarActividad)
