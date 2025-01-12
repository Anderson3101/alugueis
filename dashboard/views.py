from django.shortcuts import render
from casas.models import Casa
from alugueis.models import Aluguel
from despesas.models import Despesa
from financeiro.models import Financeiro
from django.db.models import Sum

def index(request):
    # Estatísticas gerais
    total_casas = Casa.objects.count()
    total_alugueis = Aluguel.objects.count()
    total_despesas = Despesa.objects.count()
    financeiro_totais = Financeiro.objects.aggregate(
        total_pago=Sum('total_pago'),
        total_pendente=Sum('pendencias'),
        total_despesas=Sum('total_despesas'),
        total_alugueis=Sum('total_alugueis'),
    )

    context = {
        'total_casas': total_casas,
        'total_alugueis': total_alugueis,
        'total_despesas': total_despesas,
        'total_pago': financeiro_totais.get('total_pago', 0) or 0,
        'total_pendente': financeiro_totais.get('total_pendente', 0) or 0,
        'total_despesas_fin': financeiro_totais.get('total_despesas', 0) or 0,
        'total_alugueis_fin': financeiro_totais.get('total_alugueis', 0) or 0,
    }

    return render(request, 'dashboard/index.html', context)
