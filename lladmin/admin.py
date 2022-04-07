from django.contrib import admin
from .models import cliente, equipamento
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    ...


class EquipamentoAdmin(admin.ModelAdmin):
    ...


admin.site.register(cliente, ClienteAdmin)
admin.site.register(equipamento, EquipamentoAdmin)
