from django.shortcuts import render, redirect, get_object_or_404
from .models import Casa
from .forms import CasaForm

def listar_casas(request):
    casas = Casa.objects.all()
    return render(request, 'casas/listar_casas.html', {'casas': casas})

def cadastrar_casa(request):
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_casas')
    else:
        form = CasaForm()
    return render(request, 'casas/cadastrar_casa.html', {'form': form})

def excluir_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        casa.delete()
        return redirect('listar_casas')

def editar_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        form = CasaForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            return redirect('listar_casas')
    else:
        form = CasaForm(instance=casa)
    return render(request, 'casas/editar_casa.html', {'form': form, 'casa': casa})
