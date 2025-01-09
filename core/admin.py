from django.contrib import admin
from .models import Casa, Aluguel, ConsumoEnergia, Financeiro

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')

@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('casa', 'mes_referencia', 'valor_aluguel', 'pago')

@admin.register(ConsumoEnergia)
class ConsumoEnergiaAdmin(admin.ModelAdmin):
    list_display = ('aluguel', 'leitura_anterior', 'leitura_atual', 'valor_kw', 'valor_total')

@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('aluguel', 'total_pago', 'pendente')
