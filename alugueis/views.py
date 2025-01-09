from django.shortcuts import render, redirect
from .models import Aluguel
from .forms import AluguelForm

def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'alugueis/listar_alugueis.html', {'alugueis': alugueis})

def cadastrar_aluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm()
    return render(request, 'alugueis/cadastrar_aluguel.html', {'form': form})
