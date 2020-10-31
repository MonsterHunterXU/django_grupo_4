from django.contrib import admin
from .models import Insumos, Instalaciones, Empleados, Slider, Mision, Vision

class InsumoAdmin(admin.ModelAdmin):
    list_display=['nombreinsumo','precio','descripcion']
    search_fields=['nombreinsumo','precio','descripcion']
    list_filter=['nombreinsumo','precio']
    list_per_page=10

class InstalacionesAdmin(admin.ModelAdmin):
    list_display = ['cod', 'name', 'direccion', 'imagen']
    search_fields = ['cod', 'name']
    list_per_page = 10

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['cod', 'name', 'descripcion', 'imagen']
    search_fields = ['cod', 'name']
    list_per_page = 10

class SliderAdmin(admin.ModelAdmin):
    list_display = ['cod', 'imagen']
    search_fields = ['cod']
    list_per_page = 10

class MisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'descripcion']
    search_fields = ['name']

class VisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'descripcion']
    search_fields = ['name']

# Register your models here.
admin.site.register(Insumos, InsumoAdmin)
admin.site.register(Instalaciones, InstalacionesAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)
