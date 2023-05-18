from django.contrib import admin
from apps.juicios.models import *

# Register your models here.

class TiposProcesosAdmin(admin.ModelAdmin):
    list_display = ('id','txProceso')

admin.site.register(TiposProcesos, TiposProcesosAdmin)
admin.site.register(TipoFinJuicios)
admin.site.register(SubTipoFinJuicios)
admin.site.register(UbicacionesCarpetas)
admin.site.register(TipoCarpetas)
admin.site.register(NaturalezaJuicio)
admin.site.register(EstadosCarpetas)
admin.site.register(Configuraciones)
admin.site.register(EstadosProcesales)
admin.site.register(Paises)
admin.site.register(Provincias)
admin.site.register(Localidades)
admin.site.register(TipoSiniestro)
admin.site.register(EnfermedadReclamada)
admin.site.register(Siniestros)
admin.site.register(Mandatarias)
admin.site.register(EstadoCuentaBancaria)
admin.site.register(CuentasBancarias)
admin.site.register(TipoRelacionAbogado)
admin.site.register(Abogados)
admin.site.register(JuiciosAbogados)
admin.site.register(Juicios)
admin.site.register(TipoMovimiento)
admin.site.register(Movimientos)
