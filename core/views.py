from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Casa, Aluguel, ConsumoEnergia, Financeiro
from .forms import CasaForm, AluguelForm, ConsumoEnergiaForm

def cadastrar_casa(request):
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_casas')
    else:
        form = CasaForm()
    return render(request, 'core/cadastrar_casa.html', {'form': form})

def cadastrar_aluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm()
    return render(request, 'core/cadastrar_aluguel.html', {'form': form})

def listar_casas(request):
    casas = Casa.objects.all()
    return render(request, 'core/listar_casas.html', {'casas': casas})

def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'core/listar_alugueis.html', {'alugueis': alugueis})

def detalhes_financeiros(request):
    financeiros = Financeiro.objects.all()
    return render(request, 'core/detalhes_financeiros.html', {'financeiros': financeiros})

