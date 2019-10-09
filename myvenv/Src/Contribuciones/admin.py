from django.contrib import admin

from .models import cuenta,proyecto,detalle,tipo_proyecto,persona,abono
admin.site.register(tipo_proyecto)
admin.site.register(persona)


class DetalleInline(admin.TabularInline):
    '''Tabular Inline View for Detalle'''

    model = detalle
    extra = 1

class DetalleInline_Cuenta(admin.TabularInline):
    model = abono
    extra = 1

@admin.register(proyecto)
class proyectoAdmin(admin.ModelAdmin):
    '''Admin View for Factura'''

    list_display = ('nombre','ubicacion','descripcion','fecha','total',)
    # list_filter = ('',)
    inlines = [
        DetalleInline,
    ]

@admin.register(cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre_persona','area','precio_unitario','saldo',)

    inlines = [
        DetalleInline_Cuenta,
    ]

