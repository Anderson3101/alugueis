from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from .models import Financeiro

def detalhes_financeiros(request):
    financeiros = Financeiro.objects.all()
    return render(request, 'financeiro/detalhes_financeiros.html', {'financeiros': financeiros})

def registrar_pagamento(request, pk):
    financeiro = get_object_or_404(Financeiro, pk=pk)
    if request.method == 'POST':
        # Converte o valor recebido para Decimal
        valor = Decimal(request.POST.get('valor', '0.00'))  # Garante que não seja None
        financeiro.registrar_pagamento(valor)
        return redirect('detalhes_financeiros')
    return render(request, 'financeiro/registrar_pagamento.html', {'financeiro': financeiro})
