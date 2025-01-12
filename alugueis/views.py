from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluguel
from django.contrib import messages
from decimal import Decimal

def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'alugueis/listar_alugueis.html', {'alugueis': alugueis})

def registrar_pagamento(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    if not aluguel.pago:
        aluguel.pago = True
        aluguel.save()
        messages.success(request, f'Pagamento total do aluguel da casa "{aluguel.casa.nome}" registrado com sucesso!')
    else:
        messages.warning(request, f'O aluguel da casa "{aluguel.casa.nome}" já está pago.')
    return redirect('listar_alugueis')

def registrar_pagamento_parcial(request, pk):
    aluguel = get_object_or_404(Aluguel, pk=pk)
    if request.method == 'POST':
        valor_pago = Decimal(request.POST.get('valor_pago', '0'))
        if valor_pago > 0 and valor_pago < aluguel.valor_aluguel:
            aluguel.valor_aluguel -= valor_pago
            aluguel.save()
            messages.success(request, f'Pagamento parcial de R$ {valor_pago} registrado para o aluguel da casa "{aluguel.casa.nome}".')
        else:
            messages.error(request, 'Valor inválido para pagamento parcial.')
        return redirect('listar_alugueis')
    return render(request, 'alugueis/registrar_pagamento_parcial.html', {'aluguel': aluguel})
def cadastrar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            aluguel = form.save(commit=False)
            aluguel.valor_aluguel = Decimal(aluguel.valor_aluguel)  # Converte explicitamente
            aluguel.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm()
    return render(request, 'alugueis/cadastrar_aluguel.html', {'form': form})