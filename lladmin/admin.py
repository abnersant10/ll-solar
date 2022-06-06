from django.contrib import admin
from .models import cliente, equipamento, contrato
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    ...


class ContratoAdmin(admin.ModelAdmin):
    ...


class EquipamentoAdmin(admin.ModelAdmin):
    ...


admin.site.register(cliente, ClienteAdmin)
admin.site.register(contrato, ClienteAdmin)
admin.site.register(equipamento, EquipamentoAdmin)
