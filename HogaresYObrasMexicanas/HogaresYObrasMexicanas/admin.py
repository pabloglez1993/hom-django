from django.contrib import admin
from HogaresYObrasMexicanas.models import *

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ("calle","numero","colonia","municipio","estado","codigo_postal")

@admin.register(Proyecto)
class  ProyectoAdmin(admin.ModelAdmin):
    list_display =  ("titulo","propietario","direccion","presupuesto")

@admin.register(Partida)
class  PartidaAdmin(admin.ModelAdmin):
    list_display =  ("nombre",)

@admin.register(Concepto)
class  ConceptoAdmin(admin.ModelAdmin):
    list_display =  ("nombre",)

@admin.register(Unidad)
class  UnidadAdmin(admin.ModelAdmin):
    list_display =  ("nombre","precio_unitario","sub_total")    
    
    def sub_total(self, obj):
        return obj.cantidad * obj.precio_unitario

